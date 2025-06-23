from django.shortcuts import render
from backend.django_app.flights.models import Flight, TaskResult


def last_completed_tasks(request):
    # Get last 3 successful Celery tasks from the database
    completed = TaskResult.objects.filter(status="SUCCESS").order_by('-date_done')[:3]
    tasks = [
        {
            "task_id": task.task_id,
            "status": task.status,
            "result": task.result,
        }
        for task in completed
    ]
    return render(request, "dashboard/last_completed_tasks.html", {"tasks": tasks})

def flights_table(request):
    # Get all flights from the database
    flights = Flight.objects.all()
    return render(request, "dashboard/flights_table.html", {"flights": flights})
