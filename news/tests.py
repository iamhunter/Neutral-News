import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Article

def create_article(title_text, days):
    """
    Creates a article with the given `title_text` and published the
    given number of `days` offset to now (negative for articles published
    in the past, positive for articles that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Article.objects.create(title_text=title_text, pub_date=time)



class ArticleMethodTests(TestCase):
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

    def create_article(title_text, days):
        """
        Creates a article with the given `title_text` and published the
        given number of `days` offset to now (negative for articles published
        in the past, positive for articles that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Article.objects.create(title_text=title_text, pub_date=time)


class ArticleViewTests(TestCase):
    def test_index_view_with_no_articles(self):
        """
        If no articles exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('news:indexview'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No news is available.")
        self.assertQuerysetEqual(response.context['latest_article_list'], [])

    def test_index_view_with_a_past_article(self):
        """
        Articles with a pub_date in the past should be displayed on the
        index page.
        """
        create_article(title_text="Past article.", days=-30)
        response = self.client.get(reverse('news:indexview'))
        self.assertQuerysetEqual(
            response.context['latest_article_list'],
            ['<Article: Past article.>']
        )

#    def test_index_view_with_a_future_article(self):
#        """
#        Articles with a pub_date in the future should not be displayed on
#        the index page.
#        """
#        create_article(title_text="Future article.", days=30)
#        response = self.client.get(reverse('news:index'))
#        self.assertContains(response, "No news is available.")
#        self.assertQuerysetEqual(response.context['latest_article_list'], [])
#
#    def test_index_view_with_future_article_and_past_article(self):
#        """
#        Even if both past and future articles exist, only past articles
#        should be displayed.
#        """
#        create_article(title_text="Past article.", days=-30)
#        create_article(title_text="Future article.", days=30)
#        response = self.client.get(reverse('news:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_article_list'],
#            ['<Article: Past article.>']
#        )
#
#    def test_index_view_with_two_past_articles(self):
#        """
#        The articles index page may display multiple articles.
#        """
#        create_article(title_text="Past article 1.", days=-30)
#        create_article(title_text="Past article 2.", days=-5)
#        response = self.client.get(reverse('news:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_article_list'],
#            ['<Article: Past article 2.>', '<Article: Past article 1.>']
#        )
#
#class ArticleIndexDetailTests(TestCase):
#    def test_detail_view_with_a_future_article(self):
#        """
#        The detail view of a article with a pub_date in the future should
#        return a 404 not found.
#        """
#        future_article = create_article(title_text='Future article.', days=5)
#        url = reverse('news:detail', args=(future_article.id,))
#        response = self.client.get(url)
#        self.assertEqual(response.status_code, 404)
#
#    def test_detail_view_with_a_past_article(self):
#        """
#        The detail view of a article with a pub_date in the past should
#        display the article's text.
#        """
#        past_article = create_article(title_text='Past Article.', days=-5)
#        url = reverse('news:detail', args=(past_article.id,))
#        response = self.client.get(url)
#        self.assertContains(response, past_article.title_text)
