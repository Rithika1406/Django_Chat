from django.shortcuts import render, redirect
from .models import ChatRoom, ChatMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('join-room')
    return redirect('login-user')

@login_required
def joinRoom(request):
    if request.method == "POST":
        room_name = request.POST.get("room_name")
        passcode = request.POST.get("passcode")

        try:
            room = ChatRoom.objects.get(room_name=room_name)
            if room.passcode == passcode:
                return redirect("chat-page", room_name=room_name)
            else:
                messages.error(request, "Incorrect passcode.")
        except ChatRoom.DoesNotExist:
            messages.error(request, "Room does not exist.")

    return render(request, "chat/join_room.html")

@login_required
def createRoom(request):
    if request.method == "POST":
        room_name = request.POST.get("room_name")
        passcode = request.POST.get("passcode")

        if ChatRoom.objects.filter(room_name=room_name).exists():
            messages.error(request, "Room name already taken.")
        else:
            ChatRoom.objects.create(room_name=room_name, passcode=passcode)
            messages.success(request, "Room created. You can now join it.")
            return redirect("join-room")

    return render(request, "chat/create_room.html")

@login_required
def chatPage(request, room_name):
    try:
        room = ChatRoom.objects.get(room_name=room_name)
        messages = ChatMessage.objects.filter(room=room).order_by('timestamp')[:50]
    except ChatRoom.DoesNotExist:
        messages.error(request, "Room does not exist.")
        return redirect("join-room")

    context = {
        "room_name": room_name,
        "username": request.user.username,
        "chat_messages": messages
    }
    return render(request, "chat/chat_room.html", context)