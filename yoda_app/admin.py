from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import FAQ, Article


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'link')
    summernote_fields = ('body',)