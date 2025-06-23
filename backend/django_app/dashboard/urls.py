from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.last_completed_tasks, name="last_completed_tasks"),
    path("flights/", views.flights_table, name="flights_table"),
]
