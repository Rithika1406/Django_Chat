from django.urls import path
from chatapp.consumer import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi()),
]
