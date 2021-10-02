# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.db.models import Q

class FolderQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            user=user,
            date_archived__isnull=True,
        )

    def retrieve(self, user, pk):
        result = self.filter(
                user=user,
                pk=pk
            ).first()
        if result is not None:
            return result
        else:
            raise FileNotFoundError
    
    def list_archived(self, user):
        return self.filter(
            user=user,
            date_archived__isnull=False,
        )

class FolderManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return FolderQuerySet(self.model, using=self._db)

    def list(self, user):
        return self.get_queryset().list(user)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)

    def list_archived(self, user):
        return self.get_queryset().list_archived(user)

class Folder ( models.Model ):

    objects = FolderManager()

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'folders'
    )

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    url = models.SlugField(blank=True)

    order = models.IntegerField(default=0)

    date_created = models.DateTimeField('date created', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)
    date_archived = models.DateTimeField('date archived', blank=True, null=True)

    def __str__ ( self ):
        return self.name


@receiver(post_save, sender=Folder)
def save_url(sender, instance, **kwargs):
    post_save.disconnect(save_url, sender=sender)

    instance.url = slugify(instance.name)
    instance.save()

    post_save.connect(save_url, sender=sender)

@receiver(post_save, sender=Folder)
def save_date_updated(sender, instance, **kwargs):
    post_save.disconnect(save_date_updated, sender=sender)

    instance.date_updated = timezone.now()
    instance.save()

    post_save.connect(save_date_updated, sender=sender)