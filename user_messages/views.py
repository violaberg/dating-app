from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import MessageRequest, Message, BlockedUser, Report, Conversation
from django.contrib.auth.models import User


@login_required
def message_requests(request):
    """Displays incoming message requests."""
    requests = MessageRequest.objects.filter(receiver=request.user, status="pending")
    return render(request, 'user_messages/message_requests.html', {'requests': requests})


@login_required
def send_message_request(request, user_id):
    """Allows a user to request permission to message another user."""
    receiver = get_object_or_404(User, id=user_id)

    # Check if a request already exists
    if MessageRequest.objects.filter(sender=request.user, receiver=receiver).exists():
        return JsonResponse({'error': 'Request already sent'}, status=400)

    MessageRequest.objects.create(sender=request.user, receiver=receiver)
    
    messages.success(request, f"Message request sent to {receiver.username}! ✅")
    return redirect('messages:message_requests')


@login_required
def respond_to_message_request(request, request_id, response):
    """Handles the response to a message request (accept/decline)."""
    message_request = get_object_or_404(MessageRequest, id=request_id, receiver=request.user)

    if response == 'accept':
        message_request.status = 'accepted'
        message_request.save()

    elif response == 'decline':
        message_request.status = 'declined'
        message_request.delete()

    return redirect('messages:message_requests')


@login_required
def send_message(request, user_id):
    receiver = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return redirect('messages:get_conversation', user_id=user_id)

    return redirect('messages:get_conversation', user_id=user_id)


@login_required
def get_conversation(request, user_id):
    """Fetches the chat history between two users."""
    other_user = get_object_or_404(User, id=user_id)

    messages = Message.objects.filter(
        sender=request.user, receiver=other_user
    ) | Message.objects.filter(
        sender=other_user, receiver=request.user
    ).order_by('created_at')

    return render(request, 'user_messages/conversation.html', {'messages': messages, 'other_user': other_user})


@login_required
def mark_message_read(request, message_id):
    """Marks a message as read when viewed by the receiver."""
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    message.is_read = True
    message.save()
    return JsonResponse({'status': 'read'})


@login_required
def block_user(request, user_id):
    """Blocks a user from sending messages."""
    blocked_user = get_object_or_404(User, id=user_id)

    # Prevent duplicate blocks
    if BlockedUser.objects.filter(blocker=request.user, blocked=blocked_user).exists():
        return JsonResponse({'error': 'User is already blocked'}, status=400)
    
    BlockedUser.objects.get_or_create(blocker=request.user, blocked=blocked_user)
    messages.warning(request, f"You have blocked {blocked_user.username}.")
    return redirect('messages:inbox')


@login_required
def report_message(request, message_id):
    """Allows users to report inappropriate messages."""
    message = get_object_or_404(Message, id=message_id)
    reason = request.POST.get('reason')
    
    if not reason:
        return JsonResponse({'error': 'Reason is required'}, status=400)

    Report.objects.create(reporter=request.user, message=message, reason=reason)
    messages.success(request, "Your report has been submitted.")

    return redirect('messages:message_requests')  # Redirect to message requests instead


@login_required
def inbox(request):
    """Displays the user's active conversations."""
    conversations = Conversation.objects.filter(user1=request.user) | Conversation.objects.filter(user2=request.user)
    return render(request, 'user_messages/inbox.html', {'conversations': conversations})


@login_required
def message_requests(request):
    """Displays pending message requests."""
    requests = MessageRequest.objects.filter(receiver=request.user, status='pending')
    return render(request, 'user_messages/message_requests.html', {'requests': requests})
