from django.urls import path 
from apps.news.views import form, index_home


urlpatterns = [
    path('form/', form, name = 'news_index'),
    path('objects/', index_home, name = "index_home"),
]
