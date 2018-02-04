# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('preview', models.TextField()),
                ('truth', models.TextField()),
                ('conservative_opinion', models.TextField()),
                ('liberal_opinion', models.TextField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ConservativeAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LiberalAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='news.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='conservative_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.ConservativeAuthor'),
        ),
        migrations.AddField(
            model_name='article',
            name='liberal_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.LiberalAuthor'),
        ),
    ]
