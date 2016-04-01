# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textdescription',
            name='block_text',
            field=models.TextField(verbose_name=b'Text'),
        ),
    ]
