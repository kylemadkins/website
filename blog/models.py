from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from website.blocks import ContentBlock, CodeBlock


class BlogPage(Page):
    body = StreamField(
        [("content", ContentBlock()), ("code", CodeBlock())],
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
