# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Truth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truth_text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(to='news.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='opinion',
            field=models.ManyToManyField(to='news.Opinion'),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Title'),
        ),
        migrations.AddField(
            model_name='article',
            name='truth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Truth'),
        ),
    ]
