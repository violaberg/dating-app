from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import logout
from django.contrib import messages


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
            return redirect('profile')  # Redirect to profile after saving
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
        return redirect('profile')
    
    return redirect('profile')


@login_required
def matching_profiles(request):
    """ Display all matching profiles """
    profiles = Profile.objects.all()
    return render(request, 'profiles/matching_profiles.html', {'profiles': profiles})


@login_required
def like_profile(request, profile_id):
    """
    Likes/unlikes a profile
    """
    if request.POST and 'profile_id' in request.POST:
        if 'fa-regular' in request.POST['icon_classlist_value']:
            try:
                messages.success(request, 'You liked this profile')
            except Exception:
                messages.error(
                    request, 'Sorry, an error occurred.Please try again later')
        elif 'fa-solid' in request.POST['icon_classlist_value']:
            try:
                messages.success(
                    request, 'You unliked this profile')
            except Exception:
                messages.error(
                    request, 'Sorry, an error occurred. Please try again')
    else:
        messages.error(
            request,
            'Sorry, something went wrong with bookmarking. Try again')

    return redirect(reverse('matching_profiles'))


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
        return redirect('profile')
    
    return redirect('profile')