# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CustomUser(models.Model):
    """Модель Пользователя"""
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    birthday = models.DateField('birthday', blank=True)
    email = models.EmailField("email address", blank=True)

    class Meta:
        ordering = ("id",)
