from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age', 'location')
    search_fields = ('user__username', 'location')
    list_filter = ('gender',)
    filter_horizontal = ('gender_preferences', 'age_preferences')
