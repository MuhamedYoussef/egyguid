from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date', 'image_url')
    list_display_links = ('id', 'title')
    list_editable = ('image_url',)


admin.site.register(Post, PostAdmin)
