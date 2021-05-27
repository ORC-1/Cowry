from django.urls import path
from .fetch_uuid import get_uuid


urlpatterns = [
    path('get_uuid', get_uuid, name='get_uuid')
]
