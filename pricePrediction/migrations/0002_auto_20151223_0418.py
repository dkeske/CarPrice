# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricePrediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carad',
            name='ac',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='carad',
            name='body',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='carad',
            name='gears',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='carad',
            name='km',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='carad',
            name='kw',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='carad',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='carad',
            name='year',
            field=models.CharField(max_length=20),
        ),
    ]
