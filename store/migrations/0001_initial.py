# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('url', models.URLField(blank=True)),
                ('image_url', models.URLField(blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('description', models.CharField(max_length=255)),
                ('ratingsum', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[(b'ACTION', b'Action'), (b'ADVENTURE', b'Adventure'), (b'ARCADE', b'Arcade'), (b'BOARD', b'Board'), (b'DRIVING', b'Driving'), (b'STRATEGY', b'Strategy'), (b'HORROR', b'Horror')], max_length=12)),
            ],
        ),
    ]