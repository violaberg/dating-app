from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Customizes the FAQ admin interface.

    This class specifies how the FAQ model \
    is displayed in the Django admin interface.
    """
    list_display = ('question', 'answer')
