# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-18 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='language',
        ),
    ]
