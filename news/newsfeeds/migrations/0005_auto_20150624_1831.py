# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0004_newsfeed_stared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'photos/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
