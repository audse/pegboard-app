# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

from django.utils import timezone

class Board ( models.Model ):
    
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    url = models.SlugField()

    order = models.IntegerField(default=0)

    date_created = models.DateTimeField(default=timezone.now)

    def __str__ ( self ):
        return self.name

    def create_slug ( self ):
        return slugify(self.name)
