from django.db import models

from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

from wagtail_simple_gallery.models import  SimpleGalleryIndex
    
class HomePage(Page):
   
    templates = "home/hompage_page.html"

    carousel_images = StreamField(blocks.CarouselBlock(max_num=3, required=False), blank=True, null=True)

    content = StreamField(
        [   
            ('team', blocks.TeamCards()),
            ('image', blocks.ImageBlock()),
            ("jumbotron", blocks.ActionAreaBlock()),
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        null = True, 
        blank =True, 
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("carousel_images"),
        StreamFieldPanel("content"),

    ]
    
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

