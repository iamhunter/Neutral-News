from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
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
    pub_date = models.DateTimeField('date published')
    title = models.ManyToManyField(Title)
    truth = models.ManyToManyField(Truth)
    opinion = models.ManyToManyField(Opinion)
    
    def __str__(self):
        return self.title_text