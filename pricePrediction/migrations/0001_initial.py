# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kw', models.CharField(max_length=20)),
                ('km', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('ac', models.CharField(max_length=20)),
                ('gears', models.CharField(max_length=20)),
                ('body', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('idFromSite', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CarAd1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('power', models.CharField(max_length=20)),
                ('mileage', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('airCondition', models.CharField(max_length=30)),
                ('gearBox', models.CharField(max_length=20)),
                ('chassis', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('idFromSite', models.CharField(max_length=20)),
                ('fuelType', models.CharField(max_length=20)),
            ],
        ),
    ]
