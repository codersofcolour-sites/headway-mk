# Generated by Django 3.0.7 on 2021-02-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210207_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='short_message',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
