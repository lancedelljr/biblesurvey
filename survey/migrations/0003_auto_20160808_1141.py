# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20160805_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='category',
            name='owner',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='category',
            name='purpose',
            field=models.CharField(max_length=400),
        ),
    ]
