# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0003_auto_20160415_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblbuglist',
            name='updatetime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
