# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import channels.layers
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver

class ColorQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            ( Q(user=user) | Q(board__user=user) | Q(board__shared_with=user) ),
        ).distinct()

    def retrieve(self, user, pk):
        result = self.filter(
                Q(user=user) | Q(board__user=user) | Q(board__shared_with=user),
                pk=pk
            ).first()
        if result is not None:
            return result
        else:
            raise FileNotFoundError

class ColorManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return ColorQuerySet(self.model, using=self._db)

    def list(self, user):
        return self.get_queryset().list(user)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)

class Color ( models.Model ):

    objects = ColorManager()

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='colors'
    )

    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='colors'
    )

    name = models.CharField(max_length=128)
    code = models.CharField(max_length=7)

    def __str__ ( self ):
        return self.name


@receiver(post_save, sender=Color)
def update_board_consumer(sender, instance, **kwargs):
    if instance.board:

        channel_layer = channels.layers.get_channel_layer()
        group_name = 'board-'+str(instance.board.id)+'-'+instance.board.url

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'update'
            }
        )