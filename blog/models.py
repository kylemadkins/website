from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from website.blocks import ContentBlock, CodeBlock
from website.utils import strip_tags_from_body


class BlogPage(Page):
    body = StreamField(
        [("content", ContentBlock()), ("code", CodeBlock())],
        null=True,
        blank=True,
        use_json_field=True,
    )

    @property
    def read_time(self):
        without_tags = strip_tags_from_body(self.body)
        words = without_tags.split(" ")
        wpm = len(words) // 300
        if wpm > 60:
            return f"{wpm // 60} hr, {wpm % 60} min read"
        return f"{wpm} min read"

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
