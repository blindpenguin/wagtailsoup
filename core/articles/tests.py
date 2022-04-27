from django.test import TestCase
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, rich_text

# Create your tests here.
from core.articles.models import Article
from home.models import HomePage


class ArticleTest(WagtailPageTests):
    def test_can_create_an_article(self):
        root_page = HomePage.objects.get(slug='home')

        self.assertCanCreate(root_page, Article, nested_form_data({
            'title': 'Hello World',
            'body': rich_text('<p>This is <strong>Rich Text</strong>.</p>')
        }))
