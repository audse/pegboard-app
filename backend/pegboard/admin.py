from __future__ import unicode_literals

from django.contrib import admin

from .models import Note, Tag, Checklist, Color, Comment, Page, Board, Folder, Theme

admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(Checklist)
admin.site.register(Color)
admin.site.register(Comment)
admin.site.register(Page)
admin.site.register(Board)
admin.site.register(Folder)
admin.site.register(Theme)