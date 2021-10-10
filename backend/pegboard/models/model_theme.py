# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

class ThemeQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            user=user,
        )

    def retrieve(self, user, pk):
        result = self.filter(
                 user=user,
                 pk=pk
            ).first()
        if result is not None:
            return result
        else:
            raise ObjectDoesNotExist

class ThemeManager ( models.Model ):
    use_in_migrations = True

    def get_queryset(self):
        return ThemeQuerySet(self.model, using=self._db)

    def list(self, user):
        return self.get_queryset().list(user)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)

class Theme ( models.Model ):

    objects = ThemeManager()

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'themes'
    )

    name = models.CharField(max_length=128)
    url = models.SlugField(blank=True)
    
    order = models.IntegerField(default=0)

    main = models.CharField(max_length=7)
    second = models.CharField(max_length=7)
    text = models.CharField(max_length=7)
    scale_secondary = ArrayField(
        models.CharField(max_length=7),
        size=10
    )
    scale_text = ArrayField(
        models.CharField(max_length=7),
        size=10
    )
    emphasis = models.CharField(max_length=7)
    alert = models.CharField(max_length=7)
    danger = models.CharField(max_length=7)
    
    date_created = models.DateTimeField('date created', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)
    date_archived = models.DateTimeField('date archived', blank=True, null=True)

    def __str__ ( self ):
        return self.name


@receiver(post_save, sender=Theme)
def save_url(sender, instance, **kwargs):
    post_save.disconnect(save_url, sender=sender)

    instance.url = slugify(instance.name)
    instance.save()

    post_save.connect(save_url, sender=sender)

@receiver(post_save, sender=Theme)
def save_date_updated(sender, instance, **kwargs):
    post_save.disconnect(save_date_updated, sender=sender)

    instance.date_updated = timezone.now()
    instance.save()

    post_save.connect(save_date_updated, sender=sender)