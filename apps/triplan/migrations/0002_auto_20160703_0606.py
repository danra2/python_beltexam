# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 06:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triplan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='triplan',
            old_name='user',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='triplan',
            old_name='item_product',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='triplan',
            old_name='created_at',
            new_name='travel_from',
        ),
        migrations.RenameField(
            model_name='triplan',
            old_name='updated_at',
            new_name='travel_to',
        ),
    ]
