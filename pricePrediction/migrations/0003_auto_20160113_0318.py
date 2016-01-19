# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricePrediction', '0002_auto_20160113_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='carad1',
            name='idFromSite',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carad1',
            name='mileage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carad1',
            name='power',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carad1',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carad1',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
