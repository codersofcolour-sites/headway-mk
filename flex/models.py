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
    """Flexible Page Class"""

    template = "flex/flexpage.html"
    
    banner_title = models.CharField(max_length = 100, blank = False, null = True)
    banner_subtitle = RichTextField(features = ["bold", "italic"], null = True, blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        null = True,
        blank = True,
        on_delete =models.SET_NULL,
        related_name = "+",
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",  
        null = True,
        blank = True,
        on_delete =models.SET_NULL,
        related_name = "+",
    )
    content = StreamField([("cta", blocks.CTABlock())], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ],
            heading="Banner Options",
        ),
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=10, min_num=0, label="Image")],
            heading="Carousel Images",
        ),
        StreamFieldPanel("content"),

    ]
    content = StreamField(
        [ 
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null = True, 
        blank =True, 
        
    )

    subtitle = models.CharField(max_length =100, null=True, blank=True)


    class Meta:  #noqa
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

