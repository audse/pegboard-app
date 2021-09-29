# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models import Q

class ChecklistQuerySet ( models.QuerySet ):

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

    check_items = ArrayField(
        models.JSONField(null=False, default=dict),
        blank=True,
        null=True
    )

    def __str__ ( self ):
        return self.name