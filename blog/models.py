from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    body = models.TextField()
    featured_image = models.ImageField(
        upload_to='blog_images/',
        null=True,
        blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    












