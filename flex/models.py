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

from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
# Create your models here
class FlexPage(Page):
    """Flexible Page Class"""

    template = "flex/flexpage.html"
    
    banner_overlay = ColorField(
        blank=True, 
        verbose_name='Banner Overlay Color',
        help_text='Select color of banner overlay',
        null = True
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        null = True,
        blank = True,
        on_delete =models.SET_NULL,
        related_name = "+",
    )
    
    content = StreamField(
        [ 
            ('image', blocks.ImageBlock()),
            ("jumbotron", blocks.ActionAreaBlock()),
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
        ],
        null = True, 
        blank =True,    
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                NativeColorPanel("banner_overlay"),
                ImageChooserPanel("banner_image"),
            ],
            heading="Banner Options",
        ),
        StreamFieldPanel("content"),
    ]

    class Meta: 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
