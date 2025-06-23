import asyncio
import httpx
import time
import logging
import backoff

from django.conf import settings
from celery import shared_task
from .models import TaskResult


logger = logging.getLogger(__name__)


TRAVEL_CLASS_MAP = {
    "economy": 1,
    "premium_economy": 2,
    "business": 3,
    "first": 4
}


class RateLimitException(Exception):
    pass


@backoff.on_exception(
    backoff.expo,
    RateLimitException,
    max_tries=4,
    jitter=None
)
async def fetch_retail_price(flight_data):
    def to_snake_case(s):
        return s.strip().replace(" ", "_").lower()

    params = {
        "engine": "google_flights",
        "departure_id": flight_data.get("origin"),
        "arrival_id": flight_data.get("destination"),
        "outbound_date": flight_data.get("departure_time").strftime("%Y-%m-%d"),
        "return_date": flight_data.get("arrival_time").strftime("%Y-%m-%d"),
        "travel_class": TRAVEL_CLASS_MAP.get(to_snake_case(flight_data.get("travel_class")), 1),
        "api_key": settings.SERPAPI_KEY,
    }
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(settings.SERPAPI_URL, params=params)
        if response.status_code == 429:
            raise RateLimitException("SerpAPI rate limit exceeded")
        response.raise_for_status()
        data = response.json()
        price_insights = data.get("price_insights", None)
        if price_insights is None:
            logger.info(f"No price info available for flight ID: {flight_data.get('id')}")
        return {
            "flight_id": flight_data.get("id"),
            "flight_numbers": flight_data.get("flight_numbers"),
            "origin": flight_data.get("origin"),
            "destination": flight_data.get("destination"),
            "arrival_time": flight_data.get("arrival_time").strftime("%Y-%m-%d"),
            "departure_time": flight_data.get("departure_time").strftime("%Y-%m-%d"),
            "travel_class": flight_data.get("travel_class"),
            "request_status": "success",
            "price_info": price_insights
        }

@shared_task
def enrich_flight_task(flight_data):
    try:
        start_time = time.monotonic()
        logger.info(f'Enqueuing Enrichment task for flight ID: {flight_data.get("id")}')
        result = asyncio.run(
            asyncio.wait_for(
                fetch_retail_price(flight_data),
                timeout=30
            )
        )
    except asyncio.TimeoutError:
        return {
            "flight_id": flight_data.get("id"),
            "origin": flight_data.get("origin"),
            "destination": flight_data.get("destination"),
            "status": "timeout",
            "price_info": {}
        }

    end_time = time.monotonic()
    execution_time = end_time - start_time
    logger.info(f"Enrichment task completed for flight ID {flight_data.get('id')} in {execution_time:.2f} seconds")
    TaskResult.objects.create(
        task_id = enrich_flight_task.request.id,
        status = "SUCCESS",
        result=result
    )
    return result
