# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('block_name', models.CharField(unique=True, max_length=250)),
                ('block_text', models.TextField(verbose_name=b'block of text')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('mod_date', models.DateTimeField(verbose_name=b'date last modified')),
            ],
        ),
    ]
