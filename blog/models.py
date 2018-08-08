from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, default='')

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    tag = models.ManyToManyField(Tag, related_name='posts')
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    # Admin view on site.
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
