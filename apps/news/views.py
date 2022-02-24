from django.shortcuts import render
from apps.news.models import News

# Create your views here.

def News(request):
    news=News.objects.all()
    return render(request,"index.html",{'news':news})
