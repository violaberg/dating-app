from django.shortcuts import render, redirect
from .models import ChatRoom


from django.shortcuts import render

def chat(request):
    chatrooms = ChatRoom.objects.all()  # Get all chatrooms
    return render(request, "chat/chat.html", {'chatrooms': chatrooms})


def chatroom(request, room_name):
    chatroom_exists = ChatRoom.objects.filter(name=room_name).exists()
    
    if not chatroom_exists:
        return render(request, "chat/chatroom_not_found.html", {"room_name": room_name})

    return render(request, "chat/chatroom.html", {"room_name": room_name})
