from django import forms
from django.utils.text import slugify

from .models import Post


class PostNewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

    # Override save method to implement auto-prepopulate slugfield.
    def save(self, commit=True):
        instance = super(PostNewForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance
