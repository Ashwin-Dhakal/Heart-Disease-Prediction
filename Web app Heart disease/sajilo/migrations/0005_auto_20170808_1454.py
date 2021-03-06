# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sajilo', '0004_all_hostel_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_hostel',
            name='admission_fee',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='all_hostel',
            name='deposit',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='all_hostel',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='all_hostel',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='all_hostel',
            name='latitude',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='all_hostel',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='all_hostel',
            name='longitude',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='all_hostel',
            name='monthly_charge',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='all_hostel',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='all_hostel',
            name='phone_number',
            field=models.CharField(default='', max_length=200),
        ),
    ]
