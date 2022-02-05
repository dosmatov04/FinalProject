from django.shortcuts import render
from apps.news.models import News, HomeObjects

# Create your views here.
def index_home(request):
    home = HomeObjects.objects.all()
    context = {
        'home' : home,
    }
    return render(request, 'object.html', context)

def form(request):
    return render(request, 'faq.html')