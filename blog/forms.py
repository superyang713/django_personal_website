from django import forms
from django.utils.text import slugify

from .models import Post


class PostNewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'body')

    # Override save method to implement auto-prepopulate slugfield.
    def save(self):
        instance = super(PostNewForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

        return instance
