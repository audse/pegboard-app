# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

from django.utils import timezone

class Theme ( models.Model ):

    name = models.CharField(max_length=128)
    
    order = models.IntegerField(default=0)

    primary = models.CharField(max_length=7)
    secondary = models.CharField(max_length=7)
    text = models.CharField(max_length=7)
    # scaleSecondary = models.JSONField()
    # scaleText = models.JSONField()
    
    date_created = models.DateTimeField(default=timezone.now)

    def __str__ ( self ):
        return self.name
    
    def create_slug ( self ):
        return slugify(self.name)