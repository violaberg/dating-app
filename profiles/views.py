from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
from django.http import JsonResponse

from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import logout
from django.contrib import messages
#from notifications.signals import notify
from django.contrib.auth.models import User
from notificationapp.models import Notification


@login_required
@staff_member_required
def delete_user_profile(request, user_id):
    """ Allows admin to delete a user profile and associated user account """
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        messages.success(request, f'Profile for {user.username} has been deleted.')
        return redirect('admin:index')

    return render(request, 'profiles/confirm_delete.html', {'user': user})


@login_required
def view_or_edit_profile(request):
    """ Display profile details if available, or show form to edit them. """
    profile, created = Profile.objects.get_or_create(user=request.user)

    # Check if 'edit' is in the URL query parameters
    edit_mode = request.GET.get('edit') == 'true'

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your profile details have been updated successfully!"
            )
            return redirect('profiles:profile')
        messages.error(request, "Something went wrong. Please check your inputs.")
    else:
        form = ProfileForm(instance=profile)

    return render(
        request, 'profiles/profile.html', {
            'profile': profile, 'form': form,
            'edit_mode': edit_mode, 'new_user': created
        }
    )


@login_required
def delete_profile(request):
    """ Deletes user profile but keeps account active """
    if request.method == 'POST':
        profile = request.user.profile
        # Delete profile image if it exists
        if profile.profile_image:
            profile.profile_image.delete()

        # Reset profile fields
        profile.bio = ''
        profile.gender = ''
        profile.age = None
        profile.location = ''
        profile.interests = ''
        profile.relationship_goal = ''
        profile.save()

        messages.success(request, 'Your profile has been deleted successfully.')
        return redirect('profiles:profile')

    return redirect('profiles:profile')


@login_required
def matching_profiles(request):
    user_profile = request.user.profile
    profiles = Profile.objects.exclude(user=request.user)

    if user_profile.gender_preferences.exists():
        gender_preferences = user_profile.gender_preferences.values_list('text', flat=True)
        profiles = profiles.filter(gender__in=[
            'male' if 'Men' in gender_preferences else None,
            'female' if 'Women' in gender_preferences else None,
            'non-binary' if 'Non-binary' in gender_preferences else None,
            'other' if 'Other' in gender_preferences else None
        ]).exclude(gender=None)

    if user_profile.age_preferences.exists():
        age_ranges = []
        for pref in user_profile.age_preferences.all():
            if pref.text == '18-24':
                age_ranges.extend(range(18, 25))
            elif pref.text == '25-34':
                age_ranges.extend(range(25, 35))
            elif pref.text == '35-44':
                age_ranges.extend(range(35, 45))
            elif pref.text == '45-54':
                age_ranges.extend(range(45, 55))
            elif pref.text == '55+':
                age_ranges.extend(range(55, 150))  # Using 150 as an upper bound
        profiles = profiles.filter(age__in=age_ranges)

    if user_profile.spark_type:
        profiles = profiles.filter(spark_type=user_profile.spark_type)

    profiles = profiles.prefetch_related(
        'gender_preferences',
        'age_preferences'
    ).select_related(
        'user',
        'spark_type'
    )

    return render(
        request,
        'profiles/matching_profiles.html',
        {
            'profiles': profiles,
            'user_profile': user_profile
        }
    )


@login_required
def like_profile(request, profile_id):
    """ Handles liking/unliking a profile and sends a notification """
    if request.method == "POST":
        icon_class = request.POST.get("icon_classlist_value", "")

        try:
            sender = request.user
            recipient_profile = Profile.objects.get(id=profile_id)
            recipient = recipient_profile.user

            # Prevent users from liking their own profile
            if sender == recipient:
                return JsonResponse(
                    {"success": False, "message": "You cannot like your own profile!"},
                    status=400
                )

            liked = "fa-regular" in icon_class  # Toggle based on current state
            message = (
                f"{sender.username} liked your profile ❤️"
                if liked else f"{sender.username} unliked your profile 💔"
            )

            # Create a notification only when the profile is liked
            if liked:
                Notification.objects.create(
                    recipient=recipient,
                    sender=sender,
                    message=message
                )

            response_data = {
                "success": True,
                "liked": liked,
                "message": message
            }
            return JsonResponse(response_data)

        except Profile.DoesNotExist:
            return JsonResponse(
                {"success": False, "message": "Profile not found"}, status=404
            )

        except Exception as e:
            return JsonResponse(
                {"success": False, "message": str(e)}, status=400
            )

    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)



