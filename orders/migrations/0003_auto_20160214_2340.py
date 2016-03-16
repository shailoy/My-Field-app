# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='enquiry',
            field=models.CharField(max_length=500),
        ),
    ]
