# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0012_auto_20160301_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Auth_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Auth_name',
            field=models.CharField(blank=True, max_length=200, db_index=True),
        ),
        migrations.AddField(
            model_name='product',
            name='lat',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long',
            field=models.TextField(blank=True),
        ),
    ]
