# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class CommentQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            Q(user=user) | Q(board__user=user) | Q(board__shared_with=user) | Q(page__user=user),
        )

    def retrieve(self, user, pk):
        try:
            return self.get(
                Q(user=user) | Q(board__user=user) | Q(board__shared_with=user) | Q(page__user=user) | Q(note__user=user),
                pk=pk
            )
        except Exception as e:
            return e

class CommentManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return CommentQuerySet(self.model, using=self._db)

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

    def __str__ ( self ):
        return '{self.user} {self.content}'