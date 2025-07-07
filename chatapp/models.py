from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    passcode = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name

class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return f"{self.user.username}: {self.message}"