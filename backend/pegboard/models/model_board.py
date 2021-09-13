# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Board ( models.Model ):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    url = models.SlugField()

    order = models.IntegerField(default=0)

    date_created = models.DateTimeField(default=timezone.now)

    def __str__ ( self ):
        return self.name
