from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class ContentBlock(blocks.StructBlock):
    content = blocks.RichTextBlock(
        features=[
            "h2",
            "h3",
            "h4",
            "bold",
            "italic",
            "ol",
            "ul",
            "hr",
            "link",
            "document-link",
            "image",
            "embed",
            "code",
            "blockquote",
        ]
    )

    class Meta:
        template = "blocks/content_block.html"


class CodeBlock(blocks.StructBlock):
    language = blocks.CharBlock(max_length=50)
    code = blocks.TextBlock()

    class Meta:
        template = "blocks/code_block.html"


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.RichTextBlock(features=["link"])

    class Meta:
        template = "blocks/image_block.html"


class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock()
    attribution = blocks.RichTextBlock(features=["link"])

    class Meta:
        template = "blocks/quote_block.html"
