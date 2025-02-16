from django.contrib import admin
from .models import Question, Choice, UserResponse

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'question_type', 'category_id', 'order')
    list_filter = ('question_type', 'category_id')
    search_fields = ('question_text',)
    ordering = ('order',)
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question')
    list_filter = ('question',)
    search_fields = ('text',)

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'spark_type', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username',)
    filter_horizontal = ('gender_preferences', 'age_preferences')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'spark_type')
