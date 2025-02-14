from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_or_edit_profile, name='profile'),
    path('matching/', views.matching_profiles, name='matching_profiles'),
]
