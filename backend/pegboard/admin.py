# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Card, List, Board, Theme

# Register your models here.

admin.site.register(Card)
admin.site.register(List)
admin.site.register(Board)
admin.site.register(Theme)