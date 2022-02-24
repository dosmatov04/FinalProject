from django.shortcuts import render
from apps.home.models import Setting
from apps.news.models import News

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    # phone = Phone.objects.get(pk = 1)
    news = News.objects.all()
    context = {
        'setting' : setting, 
        # 'phone' : phone,
        'news' : news,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')