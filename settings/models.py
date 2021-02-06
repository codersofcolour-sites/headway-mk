from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

class SiteTabLinkButtons(Orderable):
    page = ParentalKey('settings.BaseSettings', related_name="tab_buttons")
    button_text= models.CharField(
        max_length = 20, 
        null = True
    )
    button_url = models.URLField()

    panel = [
        FieldPanel(button_text),
        FieldPanel(button_url)
    ]

@register_setting(icon='pick')
class BaseSettings(BaseSetting, ClusterableModel):
    facebook = models.URLField(blank = True, help_text='Your Facebook page URL')
    instagram = models.URLField(blank = True, help_text='Your Instagram acount URL')
    twitter = models.URLField( blank = True, help_text='Your Twitter page URL')
    pinterest = models.URLField(blank = True,  help_text='Your pinterest page URL')
    youtube = models.URLField( blank = True, help_text='Your YouTube channel or user account URL')
    
    logo = models.ForeignKey(
        "wagtailimages.Image", 
        null = True,
        blank = False,
        on_delete =models.SET_NULL,
        related_name = "+",
    )

    address = models.CharField(
        max_length = 255, 
        blank = True, 
        null = True,
        help_text='A longer more detailed verson of address'
    )
    short_address = models.CharField(
        max_length = 36, 
        blank = True, 
        null = True,
        help_text='A short and limited version of address'
    ) 
    email = models.EmailField(blank=True)
    hours = models.CharField(
        verbose_name='Office Hours',
        max_length = 255, 
        blank = True, 
        null = True
    )
    tel = models.CharField(
        verbose_name='Phone Number',
        max_length = 20, 
        blank = True, 
        null = True
    )


    tab1= [
        ImageChooserPanel('logo')
    ]

    tab2= [
            FieldPanel('facebook'),
            FieldPanel('instagram'),
            FieldPanel('twitter'),
            FieldPanel('pinterest'),
            FieldPanel('youtube'),
    ]

    tab3= [
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('short_address'),
            FieldPanel('email'),
            FieldPanel('hours'),
            FieldPanel('tel'),
        ],heading="Details"),
        MultiFieldPanel(
            [InlinePanel("tab_buttons", max_num=3, label="Button")],
            heading="Tab link button",
        ),     
    ]

    edit_handler = TabbedInterface([
        ObjectList(tab1, heading='Site Logo'),
        ObjectList(tab2, heading='Social Media Settings'),
        ObjectList(tab3, heading='Site details'),
    ])