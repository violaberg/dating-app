from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

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
