# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reap', '0003_customer_ach_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
