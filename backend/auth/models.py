from django.db import models
from __future__ import unicode_literals
from django.contrib.auth.models import User

class Profile ( models.Model ):

    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        blank=True,
        null=True,
    )

    display_name = models.CharField(max_length=256, blank=True)

    theme = models.ForeignKey( 
        'Theme', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

# TODO model_profile.py
# @ accessibility settings: high contrast, simplified layout, etc.