# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 01:24
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


def replace_last_name_with_display_name(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    Profile = apps.get_model('judge', 'Profile')
    for row in User.objects.all():
        row.last_name = row.profile.name
        if not row.last_name:
            row.last_name = row.id

        print(row.last_name)
        row.save(update_fields=['last_name'])


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0081_unlisted_users'),
    ]

    operations = [
        migrations.RunPython(replace_last_name_with_display_name),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
