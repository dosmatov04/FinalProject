from django.urls import path 
from apps.home.views import about


urlpatterns = [
    path('about/', about, name = "about")
]