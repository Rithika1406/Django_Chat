from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth.models import User
from .models import ChatRoom, ChatMessage
from datetime import datetime
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]
        time = data["time"]
        
        # Save message to database
        user = await self.get_user(username)
        room = await self.get_room()
        if user and room:
            await self.save_message(room, user, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "sendMessage",
                "message": message,
                "username": username,
                "time": time
            }
        )

    async def sendMessage(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"],
            "time": event["time"]
        }))

    @database_sync_to_async
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @database_sync_to_async
    def get_room(self):
        try:
            return ChatRoom.objects.get(room_name=self.room_name)
        except ChatRoom.DoesNotExist:
            return None

    @database_sync_to_async
    def save_message(self, room, user, message):
        ChatMessage.objects.create(
            room=room,
            user=user,
            message=message
        )