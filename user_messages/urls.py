from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('send-request/<int:user_id>/', views.send_message_request, name='send_message_request'),
    path('respond-request/<int:request_id>/<str:response>/', views.respond_to_message_request, name='respond_message_request'),
    path('send-message/<int:user_id>/', views.send_message, name='send_message'),
    path('conversation/<int:user_id>/', views.get_conversation, name='get_conversation'),
    path('mark-read/<int:message_id>/', views.mark_message_read, name='mark_message_read'),
    path('block-user/<int:user_id>/', views.block_user, name='block_user'),
    path('report-message/<int:message_id>/', views.report_message, name='report_message'),
    path('requests/', views.message_requests, name='message_requests'),
    path('inbox/', views.inbox, name='inbox'),
]
