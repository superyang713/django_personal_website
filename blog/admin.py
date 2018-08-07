from django.contrib import admin
from . import models


admin.site.register(models.Post)
admin.site.register(models.Tag)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}
