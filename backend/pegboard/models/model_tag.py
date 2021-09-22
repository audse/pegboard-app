# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Tag ( models.Model ):

    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tags'
    )

    color = models.ForeignKey(
        'Color',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tags'
    )

    name = models.CharField(max_length=128)

    def __str__ ( self ):
        return self.name