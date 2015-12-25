# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kw', models.IntegerField()),
                ('km', models.IntegerField()),
                ('year', models.IntegerField()),
                ('ac', models.IntegerField()),
                ('gears', models.IntegerField()),
                ('body', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
