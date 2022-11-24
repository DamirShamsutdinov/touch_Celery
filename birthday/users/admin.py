# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from users.models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "birthday",
        "email"
    )
    search_fields = ("email",)
    empty_value_display = "-пусто-"
