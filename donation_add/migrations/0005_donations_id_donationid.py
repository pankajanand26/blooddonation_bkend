# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation_add', '0004_auto_20160908_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='id_donationid',
            field=models.IntegerField(default=0),
        ),
    ]
