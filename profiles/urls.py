from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_or_edit_profile, name='profile'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
]
