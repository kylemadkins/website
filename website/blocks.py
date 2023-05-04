from wagtail import blocks


class ContentBlock(blocks.StructBlock):
    content = blocks.RichTextBlock()

    class Meta:
        template = "blocks/content_block.html"


class CodeBlock(blocks.StructBlock):
    language = blocks.CharBlock(max_length=50)
    code = blocks.TextBlock()

    class Meta:
        template = "blocks/code_block.html"
