
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('news/<slug>', views.news, name='news'),
    path('flour/<level>', views.flour, name='flour'),
    path('albums', views.albums, name='albums'),
    path('album/<slug>', views.album, name='album'),



]
