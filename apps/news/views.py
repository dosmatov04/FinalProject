from django.shortcuts import render
from apps.news.models import News

# Create your views here.


def form(request):
    return render(request, 'faq.html')