# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

from django.utils import timezone

# class Card ( models.Model ):

#     list = models.ForeignKey(
#         'List',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )

#     board = models.ForeignKey(
#         'Board',
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )

#     name = models.CharField(max_length=128)
#     content = models.TextField(blank=True)

#     display = models.CharField(max_length=36)
#     url = models.SlugField()
#     order = models.IntegerField()
#     # attachment = models.FileField(upload_to='attachments/%Y/%m/%d/')

#     # Due dates are stored as charfields to parse both single dates
#     # and durations
#     date_due = models.CharField(max_length=256, blank=True)
#     date_todo = models.CharField(max_length=256, blank=True)

#     date_created = models.DateTimeField('date created', default=timezone.now)
#     date_updated = models.DateTimeField('date updated', default=timezone.now)

#     # Shows the name of the object within the admin
#     def __str__ ( self ):
#         return self.name
    
#     def create_slug ( self ):
#         return slugify(self.name)

class List ( models.Model ):

    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    url = models.SlugField()

    order = models.IntegerField(default=0)

    date_created = models.DateTimeField(default=timezone.now)

    def __str__ ( self ):
        return self.name

    def create_slug ( self ):
        return slugify(self.name)

# class Board ( models.Model ):
    
#     name = models.CharField(max_length=128)
#     description = models.TextField(blank=True)
#     url = models.SlugField()

#     order = models.IntegerField(default=0)

#     date_created = models.DateTimeField(default=timezone.now)

#     def __str__ ( self ):
#         return self.name

#     def create_slug ( self ):
#         return slugify(self.name)

# class Theme ( models.Model ):

#     name = models.CharField(max_length=128)
    
#     order = models.IntegerField(default=0)

#     primary = models.CharField(max_length=7)
#     secondary = models.CharField(max_length=7)
#     text = models.CharField(max_length=7)
#     # scaleSecondary = models.JSONField()
#     # scaleText = models.JSONField()
    
#     date_created = models.DateTimeField(default=timezone.now)

#     def __str__ ( self ):
#         return self.name
    
#     def create_slug ( self ):
#         return slugify(self.name)