# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation_add', '0010_auto_20160911_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationdetails',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='donations',
            name='id',
        ),
        migrations.RemoveField(
            model_name='donations',
            name='id_donationid',
        ),
        migrations.AddField(
            model_name='donations',
            name='donationid',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='DonationDetails',
        ),
    ]