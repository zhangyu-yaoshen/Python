# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-28 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
