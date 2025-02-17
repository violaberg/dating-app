from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('profile/', views.view_or_edit_profile, name='profile'),
    path('delete-profile/', views.delete_profile, name='delete_profile'),
    path(
        'admin/delete-profile/<int:user_id>/', 
        views.delete_user_profile, 
        name='admin_delete_profile' # Delete user profile - admin only
    ),
    path('matching/', views.matching_profiles, name='matching_profiles'),
    path(
        'matching/<int:profile_id>/favourite/',
        views.like_profile,
        name='like_profile'
    ),
]

