# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import eshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0009_remove_product_docfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(blank=True, upload_to=eshop.models.get_upload_file),
        ),
    ]
