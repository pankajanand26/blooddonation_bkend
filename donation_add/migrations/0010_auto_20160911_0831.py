# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_add', '0009_auto_20160911_0830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationdetails',
            old_name='id_donationid',
            new_name='donationid',
        ),
    ]
