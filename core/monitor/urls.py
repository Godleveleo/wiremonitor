from django.urls import path
from monitor import views
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', views.home, name="home"),    
     
    
]
