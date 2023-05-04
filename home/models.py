from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    intro_heading = models.CharField(max_length=50, blank=True, null=True)
    intro_text = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro_heading"),
        FieldPanel("intro_text")
    ]
