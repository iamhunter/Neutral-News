import datetime
import unittest

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .models import *

class ModelTests(TestCase):
    def test_was_published_recently_with_future_article(self):
        """
        was_published_recently() should return False for articles whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_article = Article(pub_date=time)
        self.assertIs(future_article.was_published_recently(), False)

    def test_was_published_recently_with_old_article(self):
        """
        was_published_recently() should return False for articles whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_article = Article(pub_date=time)
        self.assertIs(old_article.was_published_recently(), False)

    def test_was_published_recently_with_recent_article(self):
        """
        was_published_recently() should return True for articles whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_article = Article(pub_date=time)
        self.assertIs(recent_article.was_published_recently(), True)
        
    def test_article_str(self):
        """
        Creates a article
        """
        article = Article(title_text="article text")
        self.assertIs(article.__str__(), "article text")
        
class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_index_view(self):
        """
        Tests the index
        """
        index_view = self.client.get('')
        self.assertEqual(index_view.status_code, 200)
        
    def test_post_view(self):
        """
        Tests Post view. should return a 404
        """
        article = Article(title_text="article text", slug='s')
        url = reverse("post", args='s')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

        
        
