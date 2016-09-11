# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donation_add', '0016_donations_requestid'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesttable',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='donation_add.UserDetails'),
            preserve_default=False,
        ),
    ]
