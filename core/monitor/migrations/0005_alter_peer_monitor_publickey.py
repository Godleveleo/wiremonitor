# Generated by Django 4.0.3 on 2023-06-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_alter_peer_monitor_allowedips_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peer_monitor',
            name='publicKey',
            field=models.CharField(max_length=50, null=True, verbose_name='Peer'),
        ),
    ]
