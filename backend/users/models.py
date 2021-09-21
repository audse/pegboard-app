from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pegboard.models import Theme

# class SocialProfile ( models.Model ):

#     provider_id = models.CharField(max_length=256)

#     email = models.CharField(max_length=256, blank=True)
#     username = models.CharField(max_length=256, blank=True)
#     display_name = models.CharField(max_length=256, blank=True)

#     theme = models.ForeignKey( 
#         Theme, 
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )

class Profile ( models.Model ):

    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        blank=True,
        null=True
    )

    display_name = models.CharField(max_length=256, blank=True)

    theme = models.ForeignKey( 
        Theme, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

# TODO model_profile.py
# @ accessibility settings: high contrast, simplified layout, etc.