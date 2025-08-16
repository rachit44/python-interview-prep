# apps/core/urls.py
from django.urls import path
from .views import api_stats

urlpatterns = [
    path('stats/', api_stats, name='api_stats'),
]