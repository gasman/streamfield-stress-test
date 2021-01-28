from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, ListBlock, PageChooserBlock, RichTextBlock, StreamBlock, StructBlock)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class HeadingBlock(StructBlock):
    text = CharBlock(form_classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        icon = 'title'


class ImageWithCaptionBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ChoiceBlock(choices=[
        ('', 'Select alignment'),
        ('left', 'Left'),
        ('right', 'Right'),
        ('centre', 'Centre'),
    ])

    class Meta:
        icon = 'image'


class CallToActionBlock(StructBlock):
    title = CharBlock()
    image = ImageChooserBlock()
    link = PageChooserBlock()
    link_text = CharBlock()

    class Meta:
        icon = 'link'


class TestimonialBlock(StructBlock):
    photo = ImageChooserBlock()
    quote = RichTextBlock()
    attribution = CharBlock()

    class Meta:
        icon = 'openquote'


class ContentStreamBlock(StreamBlock):
    heading = HeadingBlock()
    paragraph = RichTextBlock()
    image_with_caption = ImageWithCaptionBlock()
    carousel = ListBlock(StructBlock([
        ('image', ImageChooserBlock()),
        ('caption', RichTextBlock()),
    ]), icon='arrow-right')
    call_to_action = CallToActionBlock()
    video = EmbedBlock()
    testimonial = TestimonialBlock()


class MultiColumnStreamBlock(StreamBlock):
    single_column = ContentStreamBlock()
    two_column = StructBlock([
        ('left', ContentStreamBlock()),
        ('right', ContentStreamBlock()),
    ])
    three_column = StructBlock([
        ('left', ContentStreamBlock()),
        ('middle', ContentStreamBlock()),
        ('right', ContentStreamBlock()),
    ])
