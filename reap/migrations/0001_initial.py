# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('phone', models.CharField(max_length=15)),
                ('mid', models.CharField(max_length=100)),
                ('radius', models.IntegerField(default=1)),
                ('info', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('apple_pay', models.CharField(max_length=100)),
                ('businesses', models.ManyToManyField(to='reap.Business', related_name='customers')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('amount_spent', models.IntegerField(blank=True)),
                ('discount_dollars', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('details', models.TextField(default='')),
                ('business', models.ForeignKey(to='reap.Business')),
                ('customers', models.ManyToManyField(to='reap.Customer', related_name='rewards')),
            ],
            options={
                'ordering': ('-end_date',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('amount', models.FloatField()),
                ('when', models.DateTimeField()),
                ('buyer', models.ForeignKey(to='reap.Customer')),
                ('merchant', models.ForeignKey(to='reap.Business')),
            ],
        ),
    ]
