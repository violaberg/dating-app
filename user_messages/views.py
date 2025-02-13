from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import MessageRequest, Message
from django.contrib.auth.models import User

@login_required
def send_message_request(request, user_id):
    """Allows a user to request permission to message another user."""
    receiver = get_object_or_404(User, id=user_id)

    # Check if a request already exists
    if MessageRequest.objects.filter(sender=request.user, receiver=receiver).exists():
        return JsonResponse({'error': 'Request already sent'}, status=400)

    MessageRequest.objects.create(sender=request.user, receiver=receiver)
    return JsonResponse({'message': 'Request sent successfully'}, status=200)


@login_required
def respond_to_message_request(request, request_id, response):
    """Handles the response to a message request (accept/decline)."""
    message_request = get_object_or_404(MessageRequest, id=request_id, receiver=request.user)

    if response == 'accept':
        message_request.accept()
    elif response == 'decline':
        message_request.decline()

    return JsonResponse({'status': message_request.status})


@login_required
def send_message(request, user_id):
    receiver = get_object_or_404(User, id=user_id)

    # Prevent messaging if blocked
    if BlockedUser.objects.filter(blocker=receiver, blocked=request.user).exists():
        return JsonResponse({'error': 'You have been blocked by this user'}, status=403)

    content = request.POST.get('content')
    if content:
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return JsonResponse({'message': 'Message sent successfully'})

    return JsonResponse({'error': 'Message cannot be empty'}, status=400)


@login_required
def get_conversation(request, user_id):
    """Fetches the chat history between two users."""
    other_user = get_object_or_404(User, id=user_id)

    messages = Message.objects.filter(
        sender=request.user, receiver=other_user
    ) | Message.objects.filter(
        sender=other_user, receiver=request.user
    ).order_by('created_at')

    return JsonResponse({'messages': list(messages.values())})


@login_required
def mark_message_read(request, message_id):
    """Marks a message as read when viewed by the receiver."""
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    message.mark_as_read()
    return JsonResponse({'status': 'read'})


@login_required
def block_user(request, user_id):
    """Blocks a user from sending messages."""
    blocked_user = get_object_or_404(User, id=user_id)
    BlockedUser.objects.get_or_create(blocker=request.user, blocked=blocked_user)
    return JsonResponse({'message': 'User blocked successfully'})


@login_required
def report_message(request, message_id):
    """Allows users to report inappropriate messages."""
    message = get_object_or_404(Message, id=message_id)
    reason = request.POST.get('reason')

    Report.objects.create(reporter=request.user, message=message, reason=reason)
    return JsonResponse({'message': 'Report submitted'})
