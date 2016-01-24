# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reap', '0006_auto_20151025_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='radius',
            field=models.FloatField(default=1.0),
        ),
    ]
