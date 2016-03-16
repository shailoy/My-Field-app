# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import eshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0010_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(upload_to=eshop.models.get_upload_file),
        ),
    ]
