from django.contrib import admin
from .models import Session, Character

# Register Session
admin.site.register(Session)

# Register Character
@admin.register(Character)
class SessionAdmin(admin.ModelAdmin):
    list_display = ( 'created_on',)
