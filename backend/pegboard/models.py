# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

class Card ( models.Model ):

    name = models.CharField(max_length=128)
    content = models.TextField(null=True)

    display = models.CharField(max_length=36)
    url = models.SlugField()
    order = models.IntegerField()
    # attachment = models.FileField(upload_to='attachments/%Y/%m/%d/')

    # Due dates are stored as charfields to parse both single dates
    # and durations
    date_due = models.CharField(max_length=256, blank=True)
    date_todo = models.CharField(max_length=256, blank=True)

    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')

    # Shows the name of the object within the admin
    def __str__ ( self ):
        return self.name
    
    def create_slug ( self ):
        return slugify(self.name)

# class List ( models.Model ):
    #

# class Board ( models.Model ):
    #