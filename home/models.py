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


    
class HomePage(Page):
   
    templates = "home/hompage_page.html"


    carousel_images = StreamField(blocks.CarouselBlock(max_num=3), blank=True, null=True)
    banner_title = models.CharField(max_length = 100, blank=False, null=True)
    banner_subtitle = RichTextField(features = ["bold", "italic"], null=True, blank=False)
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        null = True,
        blank = False,
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
        StreamFieldPanel("carousel_images"),
        StreamFieldPanel("content"),

    ]

    
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

    # class ColumnBlock(blocks.StreamBlock):
    #     heading = blocks.CharBlock(classname="full title")
    #     paragraph = blocks.RichTextBlock()
    #     image = ImageChooserBlock()

    # class Meta:
    #     template = 'blog/blocks/column.html'


    # class TwoColumnBlock(blocks.StructBlock):

    #     left_column = ColumnBlock(icon='arrow-right', label='Left column content')
    # right_column = ColumnBlock(icon='arrow-right', label='Right column content')

    # class Meta:
    #     template = 'blog/blocks/two_column_block.html'
    #     icon = 'placeholder'
    #     label = 'Two Columns'
    # class AlignedParagraphBlock(blocks.StructBlock):
    #     alignment = blocks.ChoiceBlock([('left', 'Left'), ('center', 'Center'), ('right', 'Right')])
    #     paragraph = blocks.RichTextBlock()

    # class Meta:
    #     template = 'blocks/aligned_paragraph.html'
    