# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.db.models import Q
import channels.layers
from asgiref.sync import async_to_sync

from .utils import DISPLAY_CHOICES


class BoardQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            Q(user=user) | Q(shared_with=user),
            date_archived__isnull=True,
        )
    
    def retrieve(self, user, pk):
        try:
            return self.get(
                Q(user=user) | Q(shared_with=user),
                pk=pk
            )
        except Exception as e:
            return e

    def retrieve_with_children(self, user, pk):
        try:
            
            response = {
                'board': None,
                'pages': [],
            }

            response['board'] = self.filter(
                Q(user=user) | Q(shared_with=user),
                date_archived__isnull=True,
                pk=pk
            ).distinct()[0]

            current_pages = response['board'].pages.all().filter(
                date_archived__isnull=True
            )


            for page in current_pages:
                all_notes_in_page = page.notes.all().filter(
                    date_archived__isnull=True
                )
                response['pages'].append({
                    'page': page,
                    'notes': all_notes_in_page
                })
            
            return response
        except Exception as e:
            print ('\n\n', 'Model Error\n\n', e, '\n\n')
            return e

    def list_archived(self, user):
        return self.filter(
            Q(user=user) | 
            Q(shared_with=user),
            date_archived__isnull=False,
        )

    def list_unsorted(self, user):
        return self.filter(
            Q(user=user) | 
            Q(shared_with=user),
            folder__isnull=True,
            date_archived__isnull=True,
        )
    
    def list_shared_with(self, user):
        return self.filter(
            shared_with=user,
            date_archived__isnull=True,
        ).exclude(
            user=user
        )

class BoardManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return BoardQuerySet(self.model, using=self._db)

    def list(self, user):
        return self.get_queryset().list(user)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)
    
    def retrieve_with_children(self, user, pk):
        return self.get_queryset().retrieve_with_children(user, pk)

    def list_archived(self, user):
        return self.get_queryset().list_archived(user)
    
    def list_unsorted(self, user):
        return self.get_queryset().list_unsorted(user)

    def list_shared_with(self, user):
        return self.get_queryset().list_shared_with(user)

class Board ( models.Model ):
    objects = BoardManager()

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'boards'
    )

    shared_with = models.ManyToManyField(
        User,
        blank=True,
        related_name = 'shared_boards',
    )

    folder = models.ForeignKey(
        'Folder',
        on_delete = models.SET_NULL,
        blank = True,
        null = True,
        related_name = 'boards'
    )
    
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    url = models.SlugField(blank=True)

    order = models.IntegerField(default=0)

    color_palette = models.ManyToManyField(
        'Color',
        blank=True,
        related_name='color_boards'
    )

    default_note_display = models.CharField(max_length=3, choices=DISPLAY_CHOICES, default='n')

    date_created = models.DateTimeField('date created', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)
    date_archived = models.DateTimeField('date archived', blank=True, null=True)

    def __str__ ( self ):
        return self.name
    
@receiver(post_save, sender=Board)
def save_shared_with(sender, instance, **kwargs):
    post_save.disconnect(save_shared_with, sender=sender)
    m2m_changed.disconnect(save_shared_with, sender=sender)

    instance.shared_with.add(instance.user)
    instance.save()

    m2m_changed.connect(save_shared_with, sender=sender)
    post_save.connect(save_shared_with, sender=sender)

@receiver(post_save, sender=Board)
def save_url(sender, instance, **kwargs):
    post_save.disconnect(save_url, sender=sender)

    instance.url = slugify(instance.name)
    instance.save()

    post_save.connect(save_url, sender=sender)

@receiver(post_save, sender=Board)
def save_date_updated(sender, instance, **kwargs):
    post_save.disconnect(save_date_updated, sender=sender)

    instance.date_updated = timezone.now()
    instance.save()

    post_save.connect(save_date_updated, sender=sender)

m2m_changed.connect(save_shared_with, sender=Board.shared_with.through)    

@receiver(post_save, sender=Board)
def update_consumer(sender, instance, **kwargs):
    channel_layer = channels.layers.get_channel_layer()
    group_name = 'board-'+str(instance.id)+'-'+instance.url
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'update'
        }
    )

# TODO model_board.py
# @ custom color palette ArrayField (for labels, etc.)
# @ theme field
