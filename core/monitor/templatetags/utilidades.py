from django import template
from monitor.models import *
from datetime import datetime
from datetime import datetime ,date, timedelta
import paramiko
register = template.Library()


@register.filter(name='estado_ssh')
def estado_ssh(id):
    objmodel = Ssh_connect.objects.filter(id__exact = id).first()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(f'{objmodel.ipHost}', username=f'{objmodel.user}', password=f'{objmodel.passwd}', port=f'{objmodel.puerto}')
        ssh_client.close()
        return True
        
    except:
        return False



