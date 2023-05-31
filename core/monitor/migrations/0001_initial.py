# Generated by Django 4.2.1 on 2023-05-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente_conf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='Nombre de cliente')),
                ('privateKey_cliente', models.CharField(max_length=50, null=True, verbose_name='clave privada cliente')),
                ('address', models.GenericIPAddressField(verbose_name='ip del cliente /24')),
                ('dns_primario', models.GenericIPAddressField(verbose_name='dns primario')),
                ('dns_secundario', models.GenericIPAddressField(verbose_name='dns secundario')),
                ('publicKey_server', models.CharField(max_length=50, null=True, verbose_name='clave publica server')),
                ('endpoint', models.GenericIPAddressField(verbose_name='Dirección ip del Server')),
            ],
            options={
                'verbose_name': 'Modelo Archivo conf Cliente VPN',
                'verbose_name_plural': 'Modelo Archivo conf Cliente VPN',
            },
        ),
        migrations.CreateModel(
            name='Peer_cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='Nombre de cliente')),
                ('publicKey', models.CharField(max_length=50, null=True, verbose_name='clave publica')),
                ('privateKey', models.CharField(max_length=50, null=True, verbose_name='clave privada')),
                ('allowedIps', models.GenericIPAddressField(verbose_name='ip del cliente')),
            ],
            options={
                'verbose_name': 'Peer cliente',
                'verbose_name_plural': 'Peer clientes',
            },
        ),
        migrations.CreateModel(
            name='Peer_server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='Nombre de cliente')),
                ('publicKey', models.CharField(max_length=50, null=True, verbose_name='clave publica')),
                ('ip_address', models.GenericIPAddressField(verbose_name='ip del server')),
                ('puerto', models.PositiveIntegerField(verbose_name='puerto escucha server')),
            ],
            options={
                'verbose_name': 'Peer cliente',
                'verbose_name_plural': 'Peer clientes',
            },
        ),
        migrations.CreateModel(
            name='Ssh_connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='Nombre Host ssh')),
                ('ipHost', models.GenericIPAddressField(verbose_name='ip host ssh')),
                ('puerto', models.PositiveIntegerField(verbose_name='puerto host ssh')),
                ('passwd', models.CharField(max_length=100, verbose_name='Contraseña ssh')),
            ],
            options={
                'verbose_name': 'Host ssh',
                'verbose_name_plural': 'Host ssh',
            },
        ),
    ]
