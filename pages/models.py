from django.db import models
from django.utils.text import slugify

class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    detail = models.TextField()
    img = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)
