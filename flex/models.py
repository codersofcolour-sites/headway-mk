"""Flex page."""


from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

from streams import blocks 
# Create your models here
class FlexPage(Page):
    template = "flex/flex_page.html"
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        default="",
        blank=True,
    )
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]
    class Meta:  # noqa
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

