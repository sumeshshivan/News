# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeeds', '0003_auto_20150621_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='stared',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
