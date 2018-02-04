import datetime
import unittest

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .models import *

class ModelTests(TestCase):        
    def test_article_str(self):
        """
        Creates an article
        """
        article = Article(title_text="article text")
        self.assertIs(article.__str__(), "article text")

    def test_conservativeauthor_str(self):
        """
        Creates a conservative author
        """
        conservative = ConservativeAuthor(first_name="first", last_name="last")
        self.assertIsNotNone(conservative.__str__())

    def test_liberalauthor_str(self):
        """
        Creates a liberal author
        """
        liberal = LiberalAuthor(first_name="first", last_name="last")
        self.assertIsNotNone(liberal.__str__())
class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

#    def test_index_view(self):
#        """
#        Tests the index
#        """
#        index_view = self.client.get('')
#        self.assertEqual(index_view.status_code, 200)

    def test_post_view(self):
        """
        Tests Post view. should return a 404
        """
        article = Article(title_text="article text", slug='s')
        url = reverse("post", args='s')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
