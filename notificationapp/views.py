from django.shortcuts import render
from .models import Notification  # Ensure you have this model
from django.contrib.auth.decorators import login_required

@login_required
def notifications_view(request):
    """ Fetch notifications for the logged-in user """
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'notificationapp/notifications.html', {'notifications': notifications})

