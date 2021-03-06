# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-18 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180518_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.TextField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(blank=True, choices=[('Java', 'Java'), ('C', 'C'), ('Python', 'Python')], max_length=30),
        ),
    ]
