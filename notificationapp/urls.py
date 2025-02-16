from django.urls import path
from . import views

app_name = "notificationapp"

urlpatterns = [
    path('', views.notifications_view, name='notifications'),
]

