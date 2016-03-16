# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0008_auto_20160215_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='docfile',
        ),
    ]
