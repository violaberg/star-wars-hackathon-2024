from django.contrib import admin
from .models import Session
# Register your models here.

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):

    list_display = ('session_name', 'created_on')
    # prepopulated_fields = {'slug': ('session_name',)}
