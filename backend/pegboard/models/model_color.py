# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class ColorQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            ( Q(user=user) | Q(board__user=user) | Q(board__shared_with=user) ),
        ).distinct()

    def retrieve(self, user, pk):
        try:
            return self.filter(
                Q(user=user) | Q(board__user=user) | Q(board__shared_with=user),
                pk=pk
            )[0]
        except Exception as e:
            return e

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
    color = models.CharField(max_length=6)

    def __str__ ( self ):
        return self.name