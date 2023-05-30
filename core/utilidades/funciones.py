import paramiko

def ejecutar_comando_remoto(comando):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('192.168.1.104', username='root', password='asnaeb123')
    stdin, stdout, stderr = ssh_client.exec_command(comando)
    resultado = stdout.read().decode('utf-8')
    ssh_client.close()
    return resultado



