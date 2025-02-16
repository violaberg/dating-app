from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
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
    """Handles sending messages and ensures conversations are created and updated"""
    receiver = get_object_or_404(User, id=user_id)

    # Ensure a conversation exists
    conversation, created = Conversation.objects.get_or_create(
        user1=min(request.user, receiver, key=lambda x: x.id),
        user2=max(request.user, receiver, key=lambda x: x.id),
    )

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                sender=request.user,
                receiver=receiver,
                conversation=conversation,  # Associate with the correct conversation
                content=content
            )
        return redirect('messages:get_conversation', user_id=user_id)

    return redirect('messages:get_conversation', user_id=user_id)


@login_required
def get_conversation(request, user_id):
    """Fetches the chat history between two users."""
    other_user = get_object_or_404(User, id=user_id)

    chat_messages = Message.objects.filter(
        sender=request.user, receiver=other_user
    ) | Message.objects.filter(
        sender=other_user, receiver=request.user
    ).order_by('created_at')

    return render(request, 'user_messages/conversation.html', {'chat_messages': chat_messages, 'other_user': other_user})


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
    """Displays the user's active conversations with the most recent message."""
    conversations = Conversation.objects.filter(
        Q(user1=request.user) | Q(user2=request.user)
    ).distinct()

    inbox_data = []
    for convo in conversations:
        # Determine the other user in the conversation
        other_user = convo.user1 if convo.user2 != request.user else convo.user2

        # Fetch the most recent message
        last_message = Message.objects.filter(conversation=convo).order_by('-created_at').first()

        inbox_data.append({
            'other_user': other_user,
            'last_message': last_message,
            'conversation_url': f"/messages/conversation/{other_user.id}/"  # Ensure correct URL
        })

    return render(request, 'user_messages/inbox.html', {'inbox_data': inbox_data})




@login_required
def message_requests(request):
    """Displays pending message requests."""
    requests = MessageRequest.objects.filter(receiver=request.user, status='pending')
    return render(request, 'user_messages/message_requests.html', {'requests': requests})
