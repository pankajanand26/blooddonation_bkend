# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 14:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donation_add', '0017_requesttable_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesttable',
            name='requestDate',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 14, 20, 0, 577350, tzinfo=utc), verbose_name='request date'),
            preserve_default=False,
        ),
    ]
