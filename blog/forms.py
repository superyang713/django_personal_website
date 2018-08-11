from django import forms
from django.utils.text import slugify

from markdownx.fields import MarkdownxFormField

from blog.models import Post, Comment


class PostNewForm(forms.ModelForm):
    Post.body = MarkdownxFormField()
    class Meta:
        model = Post
        fields = ('title', 'body', 'tag')

    # Override save method to implement auto-prepopulate slugfield.
    def save(self, commit=True):
        instance = super(PostNewForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance


class CommentForm(forms.ModelForm):
    Comment.text = MarkdownxFormField()

    class Meta:
        model = Comment
        fields = ('author', 'text')
