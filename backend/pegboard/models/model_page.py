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

class PageQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            Q(user=user) | Q(board__user=user) | Q(board__shared_with=user),
            date_archived__isnull=True,
        )

    def retrieve(self, user, pk):
        try:
            return self.filter(
                Q(user=user) | Q(board__user=user) | Q(board__shared_with=user),
                pk=pk
            )[0]
        except Exception as e:
            return e

    def list_unsorted(self, user):
        return self.filter(
            user=user,
            board__isnull=True,
            date_archived__isnull=True,
        )


class PageManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return PageQuerySet(self.model, using=self._db)

    def list(self, user):
        return self.get_queryset().list(user)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)

    def list_unsorted(self, user):
        return self.get_queryset().list_unsorted(user)


class Page ( models.Model ):

    objects = PageManager()

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'pages'
    )

    board = models.ForeignKey(
        'Board',
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'pages'
    )
    
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    url = models.SlugField(blank=True)

    order = models.IntegerField(default=0)

    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='pages'
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='assigned_pages',
    )

    date_created = models.DateTimeField('date created', default=timezone.now)
    date_updated = models.DateTimeField('date updated', default=timezone.now)
    date_archived = models.DateTimeField('date archived', blank=True, null=True)

    def __str__ ( self ):
        return self.name
    

@receiver(post_save, sender=Page)
def save_url(sender, instance, **kwargs):
    post_save.disconnect(save_url, sender=sender)

    instance.url = slugify(instance.name)
    instance.save()

    post_save.connect(save_url, sender=sender)

@receiver(post_save, sender=Page)
def save_date_updated(sender, instance, **kwargs):
    post_save.disconnect(save_date_updated, sender=sender)

    instance.date_updated = timezone.now()
    instance.save()

    post_save.connect(save_date_updated, sender=sender)

@receiver(post_save, sender=Page)
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

# TODO model_page.py
# [ ] implement children, parents