# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 10:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_add', '0014_donations'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Donor',
        ),
        migrations.DeleteModel(
            name='Requester',
        ),
    ]
