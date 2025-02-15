from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import logout
from django.contrib import messages
#from notifications.signals import notify
from django.contrib.auth.models import User


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
            messages.success(request, "Your profile details have been updated successfully!")
            return redirect('profiles:profile')  # Redirect to profile after saving
        else:
            messages.error(request, "Something went wrong. Please check your inputs.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profiles/profile.html', {'profile': profile, 'form': form, 'edit_mode': edit_mode, 'new_user': created})


@login_required
def delete_profile(request):
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
    
    return redirect('profiles:profike')


@login_required
def matching_profiles(request):
    """ Display all matching profiles """
    profiles = Profile.objects.all()
    return render(request, 'profiles/matching_profiles.html', {'profiles': profiles})


@login_required
def like_profile(request, profile_id):
    if request.method == "POST":
        icon_class = request.POST.get("icon_classlist_value", "")

        try:
            sender = request.user
            recipient_profile = Profile.objects.get(id=profile_id)
            recipient = recipient_profile.user  

            liked = "fa-regular" in icon_class  # Toggle based on current state
            message = "You liked this profile ❤️" if liked else "You unliked this profile 💔"

            response_data = {
                "success": True,
                "liked": liked,
                "message": message
            }
            print("Server Response:", json.dumps(response_data, indent=4))  # Debugging
            return JsonResponse(response_data)

        except Profile.DoesNotExist:
            return JsonResponse({"success": False, "message": "Profile not found"}, status=404)

        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=400)

    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)

