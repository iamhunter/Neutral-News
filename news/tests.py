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
        
    def test_title_str(self):
        """
        Creates a title
        """
        title = Title(title_text="title text")
        self.assertIs(title.__str__(), "title text")
        
    def test_truth_str(self):
        """
        Creates a truth
        """
        truth = Truth(truth_text="truth text")
        self.assertIs(truth.__str__(), "truth text")
        
    def test_opinion_str(self):
        """
        Creates a opinion
        """
        opinion = Opinion(opinion_text="opinion text")
        self.assertIs(opinion.__str__(), "opinion text")
        
    def test_article_str(self):
        """
        Creates a article
        """
        article = Article(title_text="article text")
        self.assertIs(article.__str__(), "article text")
        
    def test_author_str(self):
        """
        Creates a author
        """
        author = Author(first_name="firstname", last_name="lastname")
        self.assertIs(author.__str__(), "firstname")
        
class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_index_view(self):
        """
        Tests the index
        """
        index_view = self.client.get('news')
        self.assertEqual(index_view.status_code, 200)

        
        
