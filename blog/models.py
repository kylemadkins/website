from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from website.blocks import ContentBlock, CodeBlock, ImageBlock, QuoteBlock
from website.utils import strip_tags_from_body


class BlogPage(Page):
    featured_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    body = StreamField(
        [
            ("content", ContentBlock()),
            ("code", CodeBlock()),
            ("image", ImageBlock()),
            ("quote", QuoteBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )

    @property
    def read_time(self):
        words = strip_tags_from_body(str(self.body))
        time = len(words) // 200
        if time > 60:
            return f"{time // 60} hr, {time % 60} min read"
        return f"{time} min read"

    content_panels = Page.content_panels + [
        FieldPanel("featured_image"),
        FieldPanel("subtitle"),
        FieldPanel("body"),
    ]
