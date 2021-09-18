# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Card, List, Board, Theme

admin.site.register(Card)
admin.site.register(List)
admin.site.register(Board)
admin.site.register(Theme)