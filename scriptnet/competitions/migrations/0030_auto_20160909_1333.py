# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0029_auto_20160909_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]