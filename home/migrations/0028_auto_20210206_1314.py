# Generated by Django 3.0.7 on 2021-02-06 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20210206_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='carousel',
            new_name='carousel_images',
        ),
    ]
