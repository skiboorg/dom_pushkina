from django.shortcuts import render
from .models import *



def index(request):
    last_news = News.objects.all()[:3]
    albums = PhotoAlbum.objects.filter(show_at_homepage=True)[:3]
    return render(request, 'content/index.html', locals())

def about(request):
    return render(request, 'content/about.html', locals())

def flour(request,level):
    flour_level = level
    prev_level = int(level) - 1
    next_level = int(level) + 1
    if level == '2':
        prev_level = 0
    elif level == '13':
        next_level = 0
    return render(request, 'content/flour.html', locals())

def news(request,slug):
    if slug == 'all':
        news = News.objects.all()
        return render(request, 'content/news.html', locals())
    else:
        news_item = News.objects.get(slug=slug)
        return render(request, 'content/news_single.html', locals())