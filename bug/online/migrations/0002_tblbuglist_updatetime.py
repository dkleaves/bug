# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblbuglist',
            name='updatetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 15, 2, 52, 27, 982000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
