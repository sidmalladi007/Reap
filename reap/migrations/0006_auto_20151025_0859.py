# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reap', '0005_auto_20151025_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='amount_spent',
            field=models.FloatField(blank=True),
        ),
    ]
