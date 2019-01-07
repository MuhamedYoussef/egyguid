from django.db import models
from django.utils.text import slugify


class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    detail = models.TextField()
    # gmap = models.TextField(blank=True)
    sal_delay = models.IntegerField(default=400)
    img = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)
