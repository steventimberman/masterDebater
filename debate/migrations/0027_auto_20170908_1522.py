# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 20:22
from __future__ import unicode_literals

import awesome_avatar.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0026_auto_20170901_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=awesome_avatar.fields.AvatarField(blank=True, upload_to='avatars'),
        ),
    ]
