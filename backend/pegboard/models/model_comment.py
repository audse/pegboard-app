# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q

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
        if self.date_archived != None:
            return '{self.user} - {self.content}'
        else:
            return '(Archived) {self.user} - {self.content}'