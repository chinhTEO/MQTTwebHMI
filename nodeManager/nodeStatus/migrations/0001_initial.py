# Generated by Django 2.2.5 on 2019-12-20 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=120, unique=True)),
                ('topicName', models.CharField(max_length=120, unique=True)),
                ('role', models.CharField(default='subcriber', max_length=120, unique=True)),
                ('last_msg', models.CharField(max_length=120, unique=True)),
                ('lastUpdated', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('createdDate', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]