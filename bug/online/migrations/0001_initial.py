# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblBugList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=1)),
                ('describe', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=30)),
                ('belong', models.CharField(max_length=30)),
            ],
        ),
    ]
