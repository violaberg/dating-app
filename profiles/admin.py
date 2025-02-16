from django.contrib import admin
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age', 'location')
    search_fields = ('user__username', 'location')
    list_filter = ('gender',)
    filter_horizontal = ('gender_preferences', 'age_preferences')

    actions = ['delete_selected_profiles']

    def delete_selected_profiles(self, request, queryset):
        """ Allow admin to delete selected profiles and their associated user accounts """
        count = queryset.count()
        for profile in queryset:
            user = profile.user
            user.delete()
        self.message_user(request, f"Successfully deleted {count} profile(s).", messages.SUCCESS)

        return redirect(reverse('admin:profiles_profile_changelist')) # Redirect to profile list view
    
    delete_selected_profiles.short_description = "Delete selected profiles and users"
