# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20170401_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artwork',
            field=models.ImageField(blank=True, default=b'settings.MEDIA_ROOT/artworks/default_artwork.jpg', null=True, upload_to=b'artworks'),
        ),
    ]
