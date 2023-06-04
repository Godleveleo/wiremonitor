import paramiko
from monitor.models import *

def ejecutar_comando_remoto(comando):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('45.7.231.219', username='root', password='F85oiT02j4k1BBSpZg', port=22222)
    stdin, stdout, stderr = ssh_client.exec_command(comando)
    resultado = stdout.read().decode('utf-8')
    ssh_client.close()
    return resultado


def prueba_conexion():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect('45.7.231.219', username='root', password='F85oiT02j4k1BBSpZg', port=22222)
        ssh_client.close()
        return True
        
    except:
        return False

    
def cliente_monitor(output):
    cliente = {}
    lines = output.strip().split('\n')
    #lines = output.split('\n')
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

            return cliente
        
        
                



    
    
   

    
def diccionario_vacio(data):
    return len(data) == 0



