# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from monitor.models import *
from django.forms import PasswordInput
from django.core import validators


class Formulario_ssh(forms.ModelForm):
    
    class Meta:
        model = Ssh_connect
        fields = ( 'nombre','user', 'ipHost' , 'puerto', 'passwd')
        widgets = {
            
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de servidor SSH',  'autocomplete':'off'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username servidor SSH',  'autocomplete':'off'}),
            'ipHost': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección ip valida formato(0.0.0.0)',  'autocomplete':'off'}),
            'puerto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Puerto',  'autocomplete':'off','onkeypress': 'return soloNumeros(event)'}),
            'passwd': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Contraseña',  'autocomplete':'off', }),
            
            
            
        }

class Vpn_serverForm(forms.ModelForm):
    
    class Meta:
        model = Peer_server
        fields = ( 'nombre','publicKey', 'privateKey' , 'ip_address', 'puerto')
        widgets = {
            
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre VPN-server',  'autocomplete':'off'}),
            'publicKey': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'clave Publica',  'autocomplete':'off'}),
            'privateKey': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'clave privada',  'autocomplete':'off'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección ip valida formato(0.0.0.0)',  'autocomplete':'off'}),
            'puerto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Puerto',  'autocomplete':'off','onkeypress': 'return soloNumeros(event)'}),          
            
            
            
        }
        