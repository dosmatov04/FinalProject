from django.shortcuts import render
from apps.news.models import News

# Create your views here.
def news_index(request):
    news = News.objects.all()
    context = {
        'news' : news 
    }
    return render(request, 'index.html', context)

def form(request):
    return render(request, 'faq.html')