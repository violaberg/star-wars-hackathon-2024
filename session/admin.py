from django.contrib import admin
from .models import Session
# Register your models here.

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('session_name', 'slug', 'created_on')
    prepopulated_fields = {'slug': ('session_name',)}
