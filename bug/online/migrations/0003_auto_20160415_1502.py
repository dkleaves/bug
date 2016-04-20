# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0002_tblbuglist_updatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblbuglist',
            name='describe',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tblbuglist',
            name='experience',
            field=models.TextField(max_length=30),
        ),
    ]
