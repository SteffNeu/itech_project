# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antifu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=50)),
                ('from_email', models.EmailField(default=0, max_length=254)),
                ('subject', models.CharField(default=0, max_length=50)),
                ('message', models.CharField(default=0, max_length=1024)),
            ],
        ),
    ]
