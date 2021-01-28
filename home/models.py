from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from .blocks import MultiColumnStreamBlock


class HomePage(Page):
    pass


class StreamPage(Page):
    body = StreamField(MultiColumnStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
