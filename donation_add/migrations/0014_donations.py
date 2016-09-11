# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donation_add', '0013_auto_20160911_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_donationid', models.IntegerField(default=0)),
                ('donationLocation', models.CharField(max_length=200)),
                ('donationDate', models.DateTimeField(verbose_name='donation date')),
                ('requestLocation', models.CharField(max_length=200)),
                ('requestGender', models.CharField(max_length=200)),
                ('requstStatus', models.CharField(max_length=200)),
                ('trans_date', models.DateTimeField(verbose_name='transaction date')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation_add.UserDetails')),
            ],
        ),
    ]