from django.contrib import admin
from .models import Session, Character
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Session)
# admin.site.register(Character)
@admin.register(Character)
class SessionAdmin(SummernoteModelAdmin):
    list_display = ( 'created_on',)
    summernote_fields = ('description','meditation_technique_one','meditation_technique_two',)
    # prepopulated_fields = {'slug': ('session_name',)}
