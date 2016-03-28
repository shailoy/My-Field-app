# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0013_auto_20160321_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='lat',
            field=models.CharField(max_length=200, blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='long',
            field=models.CharField(max_length=200, blank=True, db_index=True),
        ),
    ]
