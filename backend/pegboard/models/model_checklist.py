# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Checklist ( models.Model ):

    # Checklists can belong to any of the data types:
    # boards, pages, or notes
    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='board'
    )
    page = models.ForeignKey(
        'Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='page'
    )
    note = models.ForeignKey(
        'Note',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='note'
    )

    name = models.CharField(max_length=128, blank=True)

    items = models.JSONField(null=False, default=dict)

    def __str__ ( self ):
        return self.name