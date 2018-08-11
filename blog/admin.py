from django.contrib import admin
from . import models
from markdownx.admin import MarkdownxModelAdmin


admin.site.register(models.Tag)
admin.site.register(models.Post, MarkdownxModelAdmin)
admin.site.register(models.Comment, MarkdownxModelAdmin)
