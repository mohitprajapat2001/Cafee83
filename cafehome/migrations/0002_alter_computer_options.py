# -*- coding: utf-8 -*-
# Generated by Django 5.0.4 on 2024-05-06 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cafehome", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="computer",
            options={"ordering": ["name"], "verbose_name": "Computer Detail"},
        ),
    ]
