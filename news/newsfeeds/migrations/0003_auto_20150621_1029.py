# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0002_auto_20150621_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='photo',
            field=models.ImageField(upload_to=b'photos/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
