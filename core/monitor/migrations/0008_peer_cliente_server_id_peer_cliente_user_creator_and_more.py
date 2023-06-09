# Generated by Django 4.2.1 on 2023-06-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_ssh_connect_user_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='peer_cliente',
            name='server_id',
            field=models.PositiveIntegerField(null=True, verbose_name='id server'),
        ),
        migrations.AddField(
            model_name='peer_cliente',
            name='user_creator',
            field=models.PositiveIntegerField(null=True, verbose_name='Usuario creador'),
        ),
        migrations.AddField(
            model_name='peer_server',
            name='user_creator',
            field=models.PositiveIntegerField(null=True, verbose_name='Usuario creador'),
        ),
        migrations.AlterField(
            model_name='peer_server',
            name='nombre',
            field=models.CharField(max_length=20, null=True, verbose_name='Nombre de servidor'),
        ),
        migrations.AlterField(
            model_name='ssh_connect',
            name='ipHost',
            field=models.GenericIPAddressField(unique=True, verbose_name='Dirección ip'),
        ),
        migrations.AlterField(
            model_name='ssh_connect',
            name='nombre',
            field=models.CharField(max_length=20, null=True, verbose_name='Nombre Conexión'),
        ),
        migrations.AlterField(
            model_name='ssh_connect',
            name='passwd',
            field=models.CharField(max_length=100, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='ssh_connect',
            name='puerto',
            field=models.PositiveIntegerField(verbose_name='Puerto'),
        ),
        migrations.AlterField(
            model_name='ssh_connect',
            name='user',
            field=models.CharField(max_length=40, null=True, verbose_name='Usuario'),
        ),
    ]
