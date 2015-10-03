# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0005_auto_20150624_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'photos/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
