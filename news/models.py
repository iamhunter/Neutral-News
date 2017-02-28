from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name
    
class Title(models.Model):
    title_text = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title_text
    
class Truth(models.Model):
    truth_text = models.TextField()
    
    def __str__(self):
        return self.truth_text
    
class Opinion(models.Model):
    opinion_text = models.TextField()
    
    def __str__(self):
        return self.opinion_text
    
class Article(models.Model):
    author = models.ManyToManyField(Author)
    title_text = models.CharField(max_length=500)
    slug = models.SlugField(max_length=100, unique=True)
    truth = models.ForeignKey(Truth, on_delete=models.CASCADE)
    opinion = models.ManyToManyField(Opinion)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
        