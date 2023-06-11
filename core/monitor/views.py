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
from utilidades.funciones import ejecutar_comando_remoto, prueba_conexion, cliente_monitor
## correo ##
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from asgiref.sync import sync_to_async
import asyncio
## correo ##


@login_required(login_url='login')
def conexiones_ssh(request):
    user = request.user.id
    datos = Ssh_connect.objects.filter(user_creator__exact=user)
    return render(request,'monitor/pages/connect-ssh.html',{'datos':datos})

@login_required(login_url='login')
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
        messages.add_message(request,messages.WARNING, "Error de conexión con el host")
        estado = False
        
    
    return render(request,'monitor/pages/connect-ssh.html',{'estado':estado,'datos':model})

@login_required(login_url='login')
def monitor_vpn(request, id):
    peer_model = Peer_monitor.objects.all().delete()
    cliente = {}
    try:
        output = ejecutar_comando_remoto(id,"wg show")     
        lines = output.strip().split('\n')
        for line in lines:   
            if "peer" in line:
                peer = line.split(':')[1].strip()                    
                cliente['peer'] = peer                      
            elif "endpoint" in line:
                endpoint = line.split(':')[1].strip()
                cliente['endpoint'] = endpoint           
            elif "allowed ips" in line:
                allowed = line.split(':')[1].strip()
                cliente['allowed_ips'] = allowed
            elif "latest handshake" in line:
                latest = line.split(':')[1].strip()
                cliente['latest_handshake'] = latest
            elif "transfer" in line:
                transfer = line.split(':')[1].strip()
                cliente['transfer'] = transfer        
                
                create = Peer_monitor.objects.create(publicKey = cliente['peer'],endpoint = cliente['endpoint'], transfer = cliente['transfer'], latest_handshake = cliente['latest_handshake'],allowedIps=cliente['allowed_ips']) 
    except:
        messages.add_message(request,messages.WARNING, "Error de conexión con el host")
        return HttpResponseRedirect('/')
        
    peer_model = Peer_monitor.objects.all()

    return render(request,'monitor/pages/monitor-vpn.html',{'peer':peer_model})