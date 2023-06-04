# Generated by Django 4.0.3 on 2023-06-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_peer_monitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peer_monitor',
            name='allowedIps',
            field=models.GenericIPAddressField(null=True, verbose_name='ip del cliente'),
        ),
        migrations.AlterField(
            model_name='peer_monitor',
            name='nombre',
            field=models.CharField(default='cliente', max_length=20, null=True, verbose_name='Nombre de cliente'),
        ),
    ]
