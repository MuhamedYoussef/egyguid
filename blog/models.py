from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=70)
    pub_date = models.DateField(default=datetime.now)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    image_url = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:110]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
