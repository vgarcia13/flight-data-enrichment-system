from django.db import models

class Flight(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    travel_class = models.CharField(max_length=20)
    origin = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_numbers = models.JSONField(default=list, blank=True)
    legs = models.JSONField(default=list, blank=True)
    last_seen = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.origin} to {self.destination} ({self.departure_time})"

class TaskResult(models.Model):
    task_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50)
    result = models.TextField()
    date_done = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_id} - {self.status}"
