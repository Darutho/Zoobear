# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-15 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170315_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='id',
            new_name='auto_increment_id',
        ),
    ]
