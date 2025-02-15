from django.contrib import admin
from .models import QuestionCategory, Question, Answer

# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category', 'question_type')
    list_filter = ('category', 'question_type')
    search_fields = ('question_text',)
    inlines = [AnswerInline]
    fieldsets = (
        (None, {'fields': ('question_text', 'category', 'question_type')}),
    )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question')
    list_filter = ('question',)
    search_fields = ('answer_text', 'question__question_text')
