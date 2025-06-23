import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")
import django

django.setup()

import logging

from fastapi import FastAPI, HTTPException
from celery.result import AsyncResult

from backend.django_app.django_app.celery import app as celery_app
from backend.django_app.flights.tasks import enrich_flight_task
from .models import FlightData


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

@app.post("/enrich-flight")
def enrich_flight(flight_data: FlightData):
    task = enrich_flight_task.delay(flight_data.model_dump())
    return {"task_id": task.id, "status": "processing"}

@app.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    if not task_result:
        raise HTTPException(status_code=404, detail="Task not found")
    if task_result.state == "PENDING":
        return {"status": "pending"}
    elif task_result.state == "SUCCESS":
        return {
            "status": "completed",
            "result": task_result.result
        }
    elif task_result.state == "FAILURE":
        return {"status": "failed", "error": str(task_result.info)}
    else:
        return {"status": task_result.state}
