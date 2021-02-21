from django.db import models

from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

from wagtail_simple_gallery.models import SimpleGalleryIndex

class GalleryPage(Page):
    template = "gallery/gallery_page.html"
    subpage_types = ["wagtail_simple_gallery.SimpleGalleryIndex"]
    max_count = 1  

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
    

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                NativeColorPanel("banner_overlay"),
                ImageChooserPanel("banner_image"),
            ],
            heading="Banner Options",
        )
    ]

SimpleGalleryIndex.parent_page_types = ["gallery.GalleryPage"]
SimpleGalleryIndex.subpage_types = []
# New default number of images displayed in gallery 
SimpleGalleryIndex._meta.get_field('images_per_page').default=32