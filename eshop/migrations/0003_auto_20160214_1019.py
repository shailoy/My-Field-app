# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_auto_20160209_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='basin',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='deposition',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.TextField(blank=True),
        ),
    ]
