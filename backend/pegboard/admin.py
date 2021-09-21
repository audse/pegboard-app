from __future__ import unicode_literals

from django.contrib import admin

from .models import Card, Page, Board, Folder, Theme

admin.site.register(Card)
admin.site.register(Page)
admin.site.register(Board)
admin.site.register(Folder)
admin.site.register(Theme)