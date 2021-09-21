# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# TODO consider renaming board

class Board ( models.Model ):

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'boards'
    )

    folder = models.ForeignKey(
        'Folder',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'boards'
    )
    
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    url = models.SlugField(blank=True)

    order = models.IntegerField(default=0)

    date_created = models.DateTimeField('date created', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)
    date_archived = models.DateTimeField('date archived', blank=True, null=True)

    def __str__ ( self ):
        return self.name
    
# TODO model_board.py
# @ implement ManyToOneField for lists
# @ custom color palette ArrayField (for labels, etc.)
# @ theme field
