# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Note ( models.Model ):

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'notes'
    )

    page = models.ForeignKey(
        'Page',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'notes'
    )

    board = models.ForeignKey(
        'Board',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'notes'
    )

    name = models.CharField(max_length=128)
    content = models.TextField(blank=True)

    display = models.CharField(max_length=36, default='note')
    url = models.SlugField(blank=True)
    order = models.IntegerField(default=0)

    # Due dates are stored as charfields to parse both single dates
    # and durations
    date_due = models.CharField(max_length=256, blank=True)
    date_todo = models.CharField(max_length=256, blank=True)

    date_created = models.DateTimeField('date created', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)
    date_archived = models.DateTimeField('date archived', blank=True, null=True)

    # Shows the name of the object within the admin
    def __str__ ( self ):
        return self.name

# TODO model_note.py
# [ ] attachment
# [ ] shared with
#     original user should be automatically added
# [ ] implement children, parents
# [ ] automatic url slugify
# [ ] board foreignkey
#     for unorganized notes
