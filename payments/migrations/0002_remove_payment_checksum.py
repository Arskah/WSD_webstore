# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-12 15:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='checksum',
        ),
    ]
