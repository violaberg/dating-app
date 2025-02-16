from django.contrib import admin
from .models import MessageRequest, Message, BlockedUser, Report, Conversation

# Register MessageRequest Model
@admin.register(MessageRequest)
class MessageRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('sender__username', 'receiver__username')

# Register Conversation Model
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'created_at')
    search_fields = ('user1__username', 'user2__username')

# Register Message Model
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'created_at', 'read')
    list_filter = ('created_at', 'read')
    search_fields = ('sender__username', 'receiver__username', 'content')

# Register BlockedUser Model
@admin.register(BlockedUser)
class BlockedUserAdmin(admin.ModelAdmin):
    list_display = ('blocker', 'blocked', 'created_at')
    search_fields = ('blocker__username', 'blocked__username')

# Register Report Model
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'message', 'reason', 'created_at')
    search_fields = ('reporter__username', 'message__content', 'reason')
