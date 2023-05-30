# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django import template
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from monitor.forms import *
from monitor.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime, date, timedelta
from django.contrib.auth.models import Group
from django.utils.timezone import utc
import datetime
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import views as auth_views
from django.utils.crypto import get_random_string
from utilidades.funciones import ejecutar_comando_remoto
## correo ##
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from asgiref.sync import sync_to_async
import asyncio
## correo ##



def home(request):
    comando = ejecutar_comando_remoto("wg")
    print(comando)
    return render(request,'monitor/pages/home.html',{'comando':comando})