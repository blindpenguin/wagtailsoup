from django.test import TestCase
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, rich_text

# Create your tests here.
from core.articles.models import Article
from home.models import HomePage


class ArticleTests(WagtailPageTests):
    def test_can_create_an_article(self):
        root_page = HomePage.objects.get(pk=2)

        self.assertCanCreate(root_page, Article, nested_form_data({
            'title': 'Hello World',
            'body': rich_text('<p>This is <strong>Rich Text</strong>.</p>')
        }))
