# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-24 21:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0010_copy_plan_repo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='repo',
        ),
    ]
