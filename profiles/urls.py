from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('profile/', views.view_or_edit_profile, name='profile'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    path('matching/', views.matching_profiles, name='matching_profiles'),
    path(
        'matching/<int:profile_id>/favourite/',
        views.like_profile,
        name='like_profile'
    ),
]

