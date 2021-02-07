# Generated by Django 3.0.7 on 2021-02-07 19:15

import datetime
from django.db import migrations, models
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210207_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='intro',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())])), ('simple_richtext', streams.blocks.SimpleRichtextBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 7, 20, 15, 46, 647982), verbose_name='Post date'),
        ),
    ]
