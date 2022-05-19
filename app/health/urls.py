"""Health urls module."""

from django.urls import path

from .views import HealthAPIView

urlpatterns = [path("health", HealthAPIView.as_view(), name="health")]
