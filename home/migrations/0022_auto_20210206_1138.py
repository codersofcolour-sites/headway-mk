# Generated by Django 3.0.7 on 2021-02-06 10:38

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210206_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='carousel',
            field=wagtail.core.fields.StreamField([('image', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('header', wagtail.core.blocks.CharBlock(max_length=40, required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Add additional text', max_length=200, required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))], icon='image')))], blank=True, null=True, verbose_name='Carousel Images'),
        ),
    ]
