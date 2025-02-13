from django.urls import path
from . import views

urlpatterns = [
    path('send-request/<int:user_id>/', views.send_message_request, name='send_message_request'),
    path('send-message/<int:user_id>/', views.send_message, name='send_message'),
]
