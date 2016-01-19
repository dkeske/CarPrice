# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricePrediction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carad1',
            name='idFromSite',
        ),
        migrations.RemoveField(
            model_name='carad1',
            name='mileage',
        ),
        migrations.RemoveField(
            model_name='carad1',
            name='power',
        ),
        migrations.RemoveField(
            model_name='carad1',
            name='price',
        ),
        migrations.RemoveField(
            model_name='carad1',
            name='year',
        ),
    ]
