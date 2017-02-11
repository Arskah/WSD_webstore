# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 17:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInventory',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='inventory', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('games', models.ManyToManyField(to='store.Game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='games', related_query_name='game', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='raters',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
