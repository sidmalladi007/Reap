# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reap', '0004_business_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='ach_token',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ach_token',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
