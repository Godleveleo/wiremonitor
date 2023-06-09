# -*- encoding: utf-8 -*-
from django.utils.html import format_html
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

class Ssh_connect(models.Model):
    user_creator = models.PositiveIntegerField(null=True, verbose_name="Usuario creador")
    nombre = models.CharField(max_length=20, null=True,  verbose_name="Nombre Conexión")
    user = models.CharField(max_length=40, null=True,  verbose_name="Usuario")
    ipHost = models.GenericIPAddressField(unique=True, verbose_name="Dirección ip")
    puerto = models.PositiveIntegerField(verbose_name="Puerto")
    passwd = models.CharField(max_length=100, verbose_name="Contraseña")


    class Meta:
        verbose_name = "Host ssh"
        verbose_name_plural = "Host ssh"

class Peer_server(models.Model):
    user_creator = models.PositiveIntegerField(null=True, verbose_name="Usuario creador")
    nombre = models.CharField(max_length=20, null=True,  verbose_name="Nombre de servidor")
    publicKey = models.CharField(max_length=50, null=True, verbose_name="clave publica")
    privateKey = models.CharField(max_length=50, null=True, verbose_name="clave privada")
    ip_address = models.GenericIPAddressField(verbose_name="ip del server")
    puerto = models.PositiveIntegerField(verbose_name="puerto escucha server") 
    

    class Meta:
        verbose_name = "Peer cliente"
        verbose_name_plural = "Peer clientes" 

    def __str__(self) :
         txt = " {0}"
         return txt.format(self.nombre) 
    
class Peer_cliente(models.Model):
    nombre = models.CharField(max_length=20, null=True,  verbose_name="Nombre de cliente")
    publicKey = models.CharField(max_length=50, null=True, verbose_name="clave publica")
    privateKey = models.CharField(max_length=50, null=True, verbose_name="clave privada")
    allowedIps = models.GenericIPAddressField(verbose_name="ip del cliente")
    user_creator = models.PositiveIntegerField(null=True, verbose_name="Usuario creador")
    server_id = models.PositiveIntegerField(null=True, verbose_name="id server")
    

    class Meta:
        verbose_name = "Peer cliente"
        verbose_name_plural = "Peer clientes" 

    def __str__(self) :
         txt = " {0}"
         return txt.format(self.nombre) 


class Peer_monitor(models.Model):
    publicKey = models.CharField( max_length=50, null=True, verbose_name="Peer")
    endpoint = models.CharField(max_length=50, null=True, verbose_name="Endpoint")
    transfer = models.CharField(max_length=50, null=True, verbose_name="Transferencia")
    latest_handshake = models.CharField(max_length=50, null=True, verbose_name="Tiempo conexion")
    allowedIps = models.GenericIPAddressField(null=True, verbose_name="ip del cliente")

def directorio_path(instance, filename): # guardar directorio con nombre del modelo nuevo
    return "carpeta/{0}/{1}".format(instance.algo, filename)
    
class cliente_conf(models.Model):   
    #interface 
    nombre = models.CharField(max_length=20, null=True,  verbose_name="Nombre de cliente")
    privateKey_cliente = models.CharField(max_length=50, null=True, verbose_name="clave privada cliente")
    address = models.GenericIPAddressField(verbose_name="ip del cliente /24")
    dns_primario = models.GenericIPAddressField(verbose_name="dns primario")
    dns_secundario = models.GenericIPAddressField(verbose_name="dns secundario")
    #peer
    publicKey_server = models.CharField(max_length=50, null=True, verbose_name="clave publica server")
    endpoint = models.GenericIPAddressField(verbose_name="Dirección ip del Server")

       
    
    class Meta:
        verbose_name = "Modelo Archivo conf Cliente VPN"
        verbose_name_plural = "Modelo Archivo conf Cliente VPN"

    

    

#@receiver(post_save, sender=cliente_conf)
#def estudiando_new(sender, instance, **kwargs):
#     if kwargs['created']:        
#         cliente_conf.objects.create(matricula=f"{instance.nombre.user.first_name} {instance.nombre.user.last_name}" ,  plan=f"{instance.plan}")


        
       
        







