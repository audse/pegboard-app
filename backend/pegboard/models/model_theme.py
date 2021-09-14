# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class Theme ( models.Model ):

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'themes'
    )

    name = models.CharField(max_length=128)
    models.SlugField(blank=True)
    
    order = models.IntegerField(default=0)

    primary = models.CharField(max_length=7)
    secondary = models.CharField(max_length=7)
    text = models.CharField(max_length=7)
    scaleSecondary = ArrayField(
        models.CharField(max_length=7),
        size=10
    )
    scaleText = ArrayField(
        models.CharField(max_length=7),
        size=10
    )
    
    date_created = models.DateTimeField('date created', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)
    date_archived = models.DateTimeField('date archived', blank=True, null=True)

    def __str__ ( self ):
        return self.name