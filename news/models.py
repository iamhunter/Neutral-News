from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class ConservativeAuthor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class LiberalAuthor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    title_text = models.CharField(max_length=500)
    image = models.ImageField()
    conservative_author = models.ForeignKey(ConservativeAuthor, on_delete=models.CASCADE)
    liberal_author = models.ForeignKey(LiberalAuthor, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    preview = models.TextField()
    truth = models.TextField()
    conservative_opinion = models.TextField()
    liberal_opinion = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
