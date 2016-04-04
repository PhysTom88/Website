# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20160401_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='textdescription',
            name='text_location',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
