# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 10:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_add', '0012_auto_20160911_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donations',
            name='userid',
        ),
        migrations.DeleteModel(
            name='Donations',
        ),
    ]
