# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20160330_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_image',
            field=models.FilePathField(default=b'/Users/Tom/Downloads/WheelerDealersTitleCard.jpg'),
        ),
    ]
