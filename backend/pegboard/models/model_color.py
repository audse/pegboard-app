# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Color ( models.Model ):

    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='colors'
    )

    name = models.CharField(max_length=128)
    color = models.CharField(max_length=6)

    def __str__ ( self ):
        return self.name