from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("dashboard/", include("backend.django_app.dashboard.urls")),
    path("api/", include("backend.django_app.flights.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
