# Generated by Django 2.2.5 on 2019-12-21 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodeStatus', '0004_auto_20191220_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodemqtt',
            name='role',
        ),
    ]