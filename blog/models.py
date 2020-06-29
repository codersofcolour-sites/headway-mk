from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

    
class BlogIndexPage(Page):
    template = "blog/blog_index_page.html" 

    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    def get_context(self, request):
        # Update context to include only published posts,
        # in reverse chronological order
        context = super(BlogIndexPage, self).get_context(request)
        live_blogpages = self.get_children().live()
        context['blogpages'] = live_blogpages.order_by('-first_published_at')
        return context
class BlogPage(Page):
    template = "blog/blog_page.html" 

    date = models.DateField("Post date")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    banner_title = models.CharField(max_length=100, blank=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        null = True,
        blank = False,
        on_delete =models.SET_NULL,
        related_name = "+",
    )
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [

        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
            ],
            heading="Banner Options",
        ),
        FieldPanel('date'),
        ImageChooserPanel('image'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    
    ]
    def get_context(self, request, *args, **kwargs):
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        context['blog_page'] = self

        context['menuitems'] = self.get_children().filter(
            live=True, show_in_menus=True)

        return context