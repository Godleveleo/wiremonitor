# -*- encoding: utf-8 -*-
from authAccount.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from django import template
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User 
from django.contrib import messages
import datetime
from django.contrib.auth.models import Group
from django.utils.timezone import utc
from django.utils.crypto import get_random_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
## correo ##
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from asgiref.sync import sync_to_async
import asyncio

def signoff(request): 
    logout(request)
    return redirect("login")


def login_user(request):    
    msg = None
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password) 
            if user is not None:                
                login(request, user)
                return redirect("/")
                
            else:
                msg = 'Credenciales invalidas'
                
        else:
            msg = 'Error en el formulario'
    else:
        form = LoginForm()

    return render(request, "auth/login.html", {"form": form, "msg": msg})


@login_required(login_url='login')
def register(request):
    msg = None
    token_generator = PasswordResetTokenGenerator()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid() and formPerfil.is_valid():
            form.save()            
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")                        
            user = authenticate(username=username, password=raw_password)
            user.is_active = False
            token = token_generator.make_token(user)
            send_mail_activeAccount(user, token)
            Token_autentificacion.objects.create(email_usuario=user, token=token)
            user.save()                       
            messages.add_message(request, messages.SUCCESS, f"Para activar tu cuenta, es necesario que confirmes tu dirección de correo electrónico. ")
            return redirect("login")
        else:            
            msg = 'Lo siento, los datos ingresados no son validos'
            
    else:
        form = SignUpForm()
        

    return render(request, "auth/account/register.html", {"form": form, 'msg':msg})



@login_required(login_url='login')
def change_passwd(request):
    msg = None
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.add_message(request, messages.SUCCESS, f"Se cambio tu contraseña.")
            return HttpResponseRedirect("/auth/login/")
        
    return render(request, "auth/change_passwd.html", {"form": form, "msg": msg})

