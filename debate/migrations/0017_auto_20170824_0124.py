# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 06:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('debate', '0016_auto_20170821_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='bad_point',
            new_name='bad_points',
        ),
        migrations.RenameField(
            model_name='point',
            old_name='good_point',
            new_name='good_points',
        ),
        migrations.AddField(
            model_name='point',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='point',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]