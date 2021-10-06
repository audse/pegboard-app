# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
import channels.layers
from asgiref.sync import async_to_sync

from .utils import DISPLAY_CHOICES

class NoteQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            Q(user=user) | Q(board__user=user) | Q(board__shared_with=user) | Q(page__user=user),
            date_archived__isnull=True
        )

    def retrieve(self, user, pk):
        result = self.filter(
                Q(user=user) | Q(board__user=user) | Q(board__shared_with=user) | Q(page__user=user),
                pk=pk
            ).first()
        if result is not None:
            return result
        else:
            raise FileNotFoundError

    def list_unsorted(self, user):
        return self.filter(
            user=user,
            page__isnull=True,
            board__isnull=True,
            date_archived__isnull=True,
        )
        

class NoteManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return NoteQuerySet(self.model, using=self._db).filter(date_archived__isnull=True).order_by('order').order_by('-date_updated')

    def list(self, user):
        return self.get_queryset().list(user)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)

    def list_unsorted(self, user):
        return self.get_queryset().list_unsorted(user)


class Note ( models.Model ):
    objects = NoteManager()

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    page = models.ForeignKey(
        'Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notes'
    )

    board = models.ForeignKey(
        'Board',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notes'
    )

    name = models.CharField(max_length=128)
    content = models.TextField(blank=True)

    display = models.CharField(max_length=3, choices=DISPLAY_CHOICES, default='n')
    url = models.SlugField(blank=True)
    order = models.IntegerField(default=0)

    starred = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    marked_done = models.BooleanField(default=False)

    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='notes'
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='assigned_notes',
    )

    # Due dates are stored as charfields to parse both single dates
    # and durations
    date_due = models.CharField(max_length=256, blank=True)
    date_todo = models.CharField(max_length=256, blank=True)

    date_created = models.DateTimeField('date created', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)
    date_archived = models.DateTimeField('date archived', blank=True, null=True)

    # Shows the name of the object within the admin
    def __str__ ( self ):
        return self.name


@receiver(post_save, sender=Note)
def save_url(sender, instance, **kwargs):
    post_save.disconnect(save_url, sender=sender)

    instance.url = slugify(instance.name)
    instance.save()

    post_save.connect(save_url, sender=sender)

@receiver(post_save, sender=Note)
def save_date_updated(sender, instance, **kwargs):
    post_save.disconnect(save_date_updated, sender=sender)

    instance.date_updated = timezone.now()
    instance.save()

    post_save.connect(save_date_updated, sender=sender)

@receiver(post_save, sender=Note)
def update_board_consumer(sender, instance, **kwargs):
    if instance.board or instance.page:

        channel_layer = channels.layers.get_channel_layer()
        group_name = 'board-'

        if instance.board:
            group_name += str(instance.board.id)+'-'+instance.board.url
        elif instance.page and instance.page.board:
            group_name += str(instance.page.board.id)+'-'+instance.page.board.url
        else:
            return

        print('\nUpdating', group_name, '...\n')

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'update'
            }
        )

# TODO model_note.py
# [ ] attachment
# [ ] implement children, parents
