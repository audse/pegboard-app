# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

from django.utils import timezone

class Profile ( models.Model ):

    display_name = models.CharField(max_length=256)

    theme = models.ForeignKey( 
        'Theme', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )