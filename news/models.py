from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    text = models.CharField(max_length=5000)
    pub_date  = models.DateTimeField('date published')
    
class Author(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    