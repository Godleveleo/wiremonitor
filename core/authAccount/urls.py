# -*- encoding: utf-8 -*-
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from authAccount import views

urlpatterns = [
    path('login/', views.login_user, name="login"),    
    path('register/', views.register, name="register"),    
    path('Signoff/', views.signoff, name="signoff"),
    ### cambio contraseña ###
    path('cambio/passwd', views.change_passwd, name= 'change-passwd'),      
       
    
]
