# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0018_point_debate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='bad_points',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='point',
            name='debate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='points', to='debate.DebateTopic'),
        ),
        migrations.AlterField(
            model_name='point',
            name='good_points',
            field=models.BigIntegerField(default=0),
        ),
    ]
