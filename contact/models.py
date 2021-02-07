from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.models import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel,MultiFieldPanel,FieldRowPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core.fields import RichTextField

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='custom_form_fields')

class ContactPage(AbstractEmailForm):
    thank_you_text = RichTextField(blank=True)
    short_message = models.CharField(blank=True, max_length=150, default='Have any inquiries, contact us!')
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
    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel(
            [
                NativeColorPanel("banner_overlay"),
                ImageChooserPanel("banner_image"),
            ],
            heading="Banner Options",
        ),
        InlinePanel('custom_form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        FieldPanel('short_message'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()