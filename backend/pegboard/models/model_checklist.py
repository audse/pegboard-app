# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
import channels.layers
from asgiref.sync import async_to_sync

class ChecklistQuerySet ( models.QuerySet ):

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

class ChecklistManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return ChecklistQuerySet(self.model, using=self._db)

    def list(self, user):
        return self.get_queryset().list(user)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)

class Checklist ( models.Model ):

    objects = ChecklistManager()

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checklists'
    )

    # Checklists can belong to any of the data types:
    # boards, pages, or notes
    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checklists'
    )
    page = models.ForeignKey(
        'Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checklists'
    )
    note = models.ForeignKey(
        'Note',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checklists'
    )

    name = models.CharField(max_length=128, blank=True)

    items = ArrayField(
        models.JSONField(null=False, default=dict),
        blank=True,
        null=True
    )

    def __str__ ( self ):
        return self.name


@receiver(post_save, sender=Checklist)
def update_board_consumer(sender, instance, **kwargs):
    if instance.board or instance.page or instance.note:

        channel_layer = channels.layers.get_channel_layer()
        group_name = 'board-'

        if instance.board:
            group_name += str(instance.board.id)+'-'+instance.board.url
        elif instance.page and instance.page.board:
            group_name += str(instance.page.board.id)+'-'+instance.page.board.url
        elif instance.note and instance.note.page and instance.note.page.board:
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