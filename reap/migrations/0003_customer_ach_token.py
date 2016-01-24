# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reap', '0002_business_ach_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='ach_token',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
