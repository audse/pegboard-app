# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Profile ( models.Model ):

    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        blank=True,
        null=True,
    )

    display_name = models.CharField(max_length=256, blank=True, null=True,)

    theme = models.ForeignKey( 
        'Theme', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )