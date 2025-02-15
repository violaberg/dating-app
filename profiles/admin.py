from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age', 'location', 'relationship_goal')
    search_fields = ('user__username', 'location', 'interests')
    list_filter = ('gender', 'relationship_goal')

