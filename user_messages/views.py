from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Message, MessageRequest
from django.contrib.auth.models import User

@login_required
def send_message_request(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    if MessageRequest.objects.filter(sender=request.user, receiver=receiver).exists():
        return JsonResponse({'error': 'Request already sent'}, status=400)

    MessageRequest.objects.create(sender=request.user, receiver=receiver)
    return JsonResponse({'message': 'Request sent successfully'}, status=200)

@login_required
def send_message(request, user_id):
    receiver = get_object_or_404(User, id=user_id)

    if not MessageRequest.objects.filter(sender=receiver, receiver=request.user, status='accepted').exists():
        return JsonResponse({'error': 'Permission denied'}, status=403)

    content = request.POST.get('content')
    if content:
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return JsonResponse({'message': 'Message sent successfully'})

    return JsonResponse({'error': 'Message cannot be empty'}, status=400)
