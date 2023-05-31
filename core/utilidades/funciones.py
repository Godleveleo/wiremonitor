import paramiko

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

    
     



