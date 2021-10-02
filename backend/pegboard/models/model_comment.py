# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
import channels.layers
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver

class CommentQuerySet ( models.QuerySet ):

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

class CommentManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return CommentQuerySet(self.model, using=self._db).filter(date_archived__isnull=True)

    def list(self, user):
        return self.get_queryset().list(user)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)

class Comment ( models.Model ):

    objects = CommentManager()

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments'
    )

    page = models.ForeignKey(
        'Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments'
    )

    note = models.ForeignKey(
        'Note',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments'
    )

    content = models.CharField(max_length=128)

    date_created = models.DateTimeField('date created', default=timezone.now)
    date_edited = models.DateTimeField('date edited', blank=True, null=True)
    date_archived = models.DateTimeField('date archived', blank=True, null=True)

    def __str__ ( self ):
        if self.date_archived is None:
            return '{self.user} - {self.content}'.format(**vars())
        else:
            return '(Archived) {self.user} - {self.content}'.format(**vars())

@receiver(post_save, sender=Comment)
def update_board_consumer(sender, instance, **kwargs):
    if instance.board or instance.page or instance.note:

        channel_layer = channels.layers.get_channel_layer()
        group_name = 'board-'

        if instance.board:
            group_name += str(instance.board.id)+'-'+instance.board.url
        elif instance.page:
            group_name += str(instance.page.board.id)+'-'+instance.page.board.url
        elif instance.note and instance.note.page:
            group_name += str(instance.note.page.board.id)+'-'+instance.note.page.board.url
        elif instance.note and instance.note.board:
            group_name += str(instance.note.board.id)+'-'+instance.note.board.url
        else:
            return

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'update'
            }
        )