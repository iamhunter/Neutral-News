from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = 'title_text', 'slug', 'conservative_opinion'
    prepopulated_fields = {"slug": ("title_text",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(ConservativeAuthor)
admin.site.register(LiberalAuthor)
admin.site.register(Category)
