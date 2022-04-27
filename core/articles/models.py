from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


# Articles are meant to be used as basic pages like Imprint or About Us.
# They're called "Articles", because "Page" is already taken by Wagtail and "BasePage" sounds dumb.
class Article(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

    api_fields = [
        APIField('body')
    ]
