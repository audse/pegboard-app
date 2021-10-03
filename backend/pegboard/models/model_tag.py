# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import channels.layers
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver

class TagQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            Q(user=user) | Q(board__user=user) | Q(board__shared_with=user) | Q(page__user=user),
        )

    def retrieve(self, user, pk):
        result = self.filter(
                Q(user=user) | Q(board__user=user) | Q(board__shared_with=user) | Q(page__user=user) | Q(note__user=user),
                pk=pk
            ).first()
        if result is not None:
            return result
        else:
            raise FileNotFoundError

class TagManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return TagQuerySet(self.model, using=self._db)

    def list(self, user):
        return self.get_queryset().list(user)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)

class Tag ( models.Model ):

    objects = TagManager()

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tags'
    )

    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tags'
    )

    color = models.ForeignKey(
        'Color',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tags'
    )

    name = models.CharField(max_length=128)

    def __str__ ( self ):
        return self.name

@receiver(post_save, sender=Tag)
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