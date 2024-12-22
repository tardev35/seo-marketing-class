from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)







