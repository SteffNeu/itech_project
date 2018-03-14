# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 08:14
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('comment', models.TextField(max_length=1024)),
                ('loveliness', models.IntegerField(default=0)),
                ('burnfactor', models.IntegerField(default=0)),
                ('logicRating', models.IntegerField(default=0)),
                ('accuracyRating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField(blank=True)),
                ('answers', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('href', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=64)),
                ('context', models.TextField(max_length=512)),
                ('tags', models.CharField(max_length=128)),
                ('grammarFail', models.IntegerField(default=0)),
                ('logicFail', models.IntegerField(default=0)),
                ('toxicity', models.IntegerField(default=0)),
                ('harmful', models.IntegerField(default=0)),
                ('report', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('picturePost', models.ImageField(upload_to='post_pictures')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='antifu.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('totallove', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='antifu.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='antifu.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='antifu.UserProfile'),
        ),
    ]
