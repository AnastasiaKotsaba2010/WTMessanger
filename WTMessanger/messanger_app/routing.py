from django.urls import path
from .consumers import ChatConsumer

ws_urlpatterns = [
    path("chat/<int:group_id>", ChatConsumer.as_asgi()) 
]