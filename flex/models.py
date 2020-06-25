"""Flex page."""


from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
# Create your models here
class FlexPage(Page):
    """Flexible Page Class"""

    template = "flex/flexpage.html"
    # @todo add streamfield
    #content = Streamfield()

    subtitle = models.CharField(max_length =100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:  #noqa
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

