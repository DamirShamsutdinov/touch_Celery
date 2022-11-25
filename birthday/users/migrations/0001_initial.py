# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-24 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('birthday', models.DateField(blank=True, verbose_name='birthday')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
