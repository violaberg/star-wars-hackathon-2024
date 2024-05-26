from django.contrib import admin
from .models import Session, Character

admin.site.register(Session)
# admin.site.register(Character)
@admin.register(Character)
class SessionAdmin(admin.ModelAdmin):
    list_display = ( 'created_on',)
