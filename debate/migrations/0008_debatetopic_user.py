# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0007_auto_20170807_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='debatetopic',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='debate.UserProfile'),
            preserve_default=False,
        ),
    ]
