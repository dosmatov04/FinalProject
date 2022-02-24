from django.urls import path 
from apps.news.views import News

urlpatterns = [
    path('index/',News,name="creative")
]

