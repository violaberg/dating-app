from django.contrib import admin
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age', 'location', 'spark_type')
    search_fields = ('user__username', 'location')
    list_filter = ('gender',)
    filter_horizontal = ('gender_preferences', 'age_preferences')

    actions = ['delete_selected_profiles']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """ Ensure gender_preferences and age_preferences show the correct choices """
        if db_field.name == "gender_preferences":
            kwargs["queryset"] = db_field.related_model.objects.filter(
                text__in=["Men", "Women", "Non-binary", "Other"]
            )
        elif db_field.name == "age_preferences":
            kwargs["queryset"] = db_field.related_model.objects.filter(
                text__in=["18-24", "25-34", "35-44", "45-54", "55+"]
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """ Ensure spark_type dropdown only displays relationship types """
        if db_field.name == "spark_type":
            kwargs["queryset"] = db_field.related_model.objects.filter(
                text__in=["Long-term Relationship", "Casual Dating", "Marriage", "Friendship"]
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def delete_selected_profiles(self, request, queryset):
        """ Allow admin to delete selected profiles and their associated user accounts """
        count = queryset.count()
        for profile in queryset:
            user = profile.user
            user.delete()
        self.message_user(request, f"Successfully deleted {count} profile(s).", messages.SUCCESS)

        return redirect(reverse('admin:profiles_profile_changelist')) # Redirect to profile list view
    
    delete_selected_profiles.short_description = "Delete selected profiles and users"
