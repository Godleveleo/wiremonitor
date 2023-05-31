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
import paramiko
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import views as auth_views
from django.utils.crypto import get_random_string
from utilidades.funciones import ejecutar_comando_remoto, prueba_conexion
## correo ##
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from asgiref.sync import sync_to_async
import asyncio
## correo ##



def conexiones_ssh(request):
    datos = Ssh_connect.objects.all()
    return render(request,'monitor/pages/connect-ssh.html',{'datos':datos})

def estado_ssh(request, id):
    estado = None
    model = Ssh_connect.objects.filter(id__exact = id)
    objmodel = model.first()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(f'{objmodel.ipHost}', username=f'{objmodel.user}', password=f'{objmodel.passwd}', port=f'{objmodel.puerto}')
        ssh_client.close()        
        estado = True

    except:
        estado = False
        
    
    return render(request,'monitor/pages/connect-ssh.html',{'estado':estado,'datos':model})

def monitor_vpn(request):
    output = ejecutar_comando_remoto("wg show")
    
    status_data = []
    peer = []
    lines = output.strip().split('\n')
    for line in lines:        
        status_data.append(line)
        if "peer" in line:
            peer.append(line)

    return render(request,'monitor/pages/monitor-vpn.html',{'data':status_data, 'peer':peer})