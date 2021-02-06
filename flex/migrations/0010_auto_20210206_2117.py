# Generated by Django 3.0.7 on 2021-02-06 20:17

from django.db import migrations
import wagtail_color_panel.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0009_auto_20210206_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flexpage',
            name='banner_title',
        ),
        migrations.RemoveField(
            model_name='flexpage',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='flexpage',
            name='banner_overlay',
            field=wagtail_color_panel.fields.ColorField(help_text='Select color of banner overlay', max_length=7, null=True, verbose_name='Banner Overlay Color'),
        ),
    ]