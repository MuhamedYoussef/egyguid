from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('city/<slug:slug>', views.city, name='city'),
    path('about', views.about, name='about')
]
