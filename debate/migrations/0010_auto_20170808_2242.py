# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0009_auto_20170807_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debatetopic',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
