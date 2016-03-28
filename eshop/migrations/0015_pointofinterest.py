# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0014_auto_20160321_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
    ]
