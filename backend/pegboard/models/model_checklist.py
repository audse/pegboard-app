# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Checklist ( models.Model ):

    # Checklists can belong to any of the data types:
    # boards, pages, or notes
    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checklists'
    )
    page = models.ForeignKey(
        'Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checklists'
    )
    note = models.ForeignKey(
        'Note',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checklists'
    )

    name = models.CharField(max_length=128, blank=True)

    check_items = ArrayField(
        models.JSONField(null=False, default=dict),
        blank=True,
        null=True
    )

    def __str__ ( self ):
        return self.name