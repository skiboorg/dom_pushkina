from django.shortcuts import render
from .models import *



def index(request):
    last_news = News.objects.all()[:3]
    return render(request, 'content/index.html', locals())