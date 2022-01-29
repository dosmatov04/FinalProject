from django.urls import path 
from apps.news.views import form


urlpatterns = [
    path('form/', form, name = 'news_index')
]
