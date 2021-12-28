from django.urls import path 
from apps.news.views import news_index


urlpatterns = [
    path('', news_index, name = 'news_index')
]
