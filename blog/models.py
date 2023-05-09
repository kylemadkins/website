from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TagBase, ItemBase

from website.blocks import ContentBlock, CodeBlock, ImageBlock, QuoteBlock
from website.utils import strip_tags_from_body


@register_snippet
class BlogTag(TagBase):
    free_tagging = False
    text_color = models.CharField(max_length=50, help_text="A CSS color for the tag text", null=True, blank=True)
    border_color = models.CharField(max_length=50, help_text="A CSS color for the tag border", null=True, blank=True)
    background_color = models.CharField(max_length=50, help_text="A CSS color for the tag background", null=True, blank=True)


class TaggedBlog(ItemBase):
    tag = models.ForeignKey(
        BlogTag, related_name="tagged_blogs", on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        to="BlogPage",
        on_delete=models.CASCADE,
        related_name="tagged_items"
    )


class BlogPage(Page):
    tags = ClusterTaggableManager(through=TaggedBlog, blank=True)
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
        FieldPanel("tags"),
        FieldPanel("featured_image"),
        FieldPanel("subtitle"),
        FieldPanel("body"),
    ]
