from django.db import models
from django.urls import reverse
from django.utils import timezone

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = MarkdownxField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=140, unique=True)
    tag = models.ManyToManyField(Tag, related_name='posts')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    # Admin view on site.
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments'
    )
    author = models.CharField(max_length=200)
    text = MarkdownxField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    @property
    def formatted_markdown(self):
        return markdownify(self.text)

    def __str__(self):
        return self.text
