from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body = models.TextField()
    featured_image = models.ImageField(
        upload_to='blog_images/',
        null=True,
        blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


# blog/templates/blog/home.html







