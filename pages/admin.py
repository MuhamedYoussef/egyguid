from django.contrib import admin
from .models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'img')
    list_display_links = ('id', 'name')
    list_editable = ('img',)

admin.site.register(City, CityAdmin)
