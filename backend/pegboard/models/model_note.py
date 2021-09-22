# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.db.models import Q

class NoteQuerySet ( models.QuerySet ):

    def list(self, user):
        return self.filter(
            Q(user=user) | Q(shared_with=user),
            date_archived__isnull=True,
        )

    def retrieve(self, user, pk):
        try:
            return self.get(
                Q(user=user) | Q(shared_with=user),
                date_archived__isnull=True,
                pk=pk
            )
        except Exception as e:
            return e
        
    def list_by_page(self, user, page):
        return self.filter(
            Q(user=user) | Q(shared_with=user),
            date_archived__isnull=True,
            page=page
        )
        
    def list_by_board(self, user, board):
        return self.filter(
            Q(user=user) | Q(shared_with=user),
            date_archived__isnull=True,
            board=board
        )

    def list_by_tag(self, user, tag):
        return self.filter(
            Q(user=user) | Q(shared_with=user),
            date_archived__isnull=True,
            tag=tag
        )

    def list_unsorted(self, user):
        return self.filter(
            Q(user=user) | Q(shared_with=user),
            page__isnull=True,
            date_archived__isnull=True,
        )

    def list_archived(self, user):
        return self.filter(
            Q(user=user) | Q(shared_with=user),
            date_archived__isnull=False,
        )
    
    def retrieve_archived(self, user, pk):
        try:
            return self.get(
                Q(user=user) | Q(shared_with=user),
                date_archived__isnull=False,
                pk=pk
            )
        except Exception as e:
            return e
    
    def list_shared_with(self, user):
        return self.filter(
            shared_with=user,
            date_archived__isnull=True,
        ).exclude(
            user=user
        )

class NoteManager ( models.Manager ):
    use_in_migrations = True

    def get_queryset(self):
        return NoteQuerySet(self.model, using=self._db)

    def list(self, user):
        return self.get_queryset().list(user)

    def list_by_page(self, user, page):
        return self.get_queryset().list_by_page(user, page)

    def list_by_board(self, user, board):
        return self.get_queryset().list_by_board(user, board)

    def list_by_tag(self, user, tag):
        return self.get_queryset().list_by_tag(user, tag)

    def retrieve(self, user, pk):
        return self.get_queryset().retrieve(user, pk)

    def list_unsorted(self, user):
        return self.get_queryset().list_unsorted(user)

    def list_archived(self, user):
        return self.get_queryset().list_archived(user)

    def retrieve_archived(self, user, pk):
        return self.get_queryset().retrieve_archived(user, pk)

    def list_shared_with(self, user):
        return self.get_queryset().list_shared_with(user)

class Note ( models.Model ):
    objects = NoteManager()

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    shared_with = models.ManyToManyField(
        User,
        blank=True,
        related_name='shared_notes',
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

    DISPLAY_CHOICES = [
        ('n', 'note'),
        ('h', 'heading'),
        ('i', 'image'),
        ('c', 'checkbox'),
        ('a', 'assignee'),
    ]

    display = models.CharField(max_length=36, choices=DISPLAY_CHOICES, default='n')
    url = models.SlugField(blank=True)
    order = models.IntegerField(default=0)

    marked_done = models.BooleanField(default=False)

    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='tag'
    )

    checklist = models.ForeignKey(
        'Checklist',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checklist'
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
def save_shared_with(sender, instance, **kwargs):
    post_save.disconnect(save_shared_with, sender=sender)
    m2m_changed.disconnect(save_shared_with, sender=sender)

    instance.shared_with.add(instance.user)
    instance.save()

    m2m_changed.connect(save_shared_with, sender=sender)
    post_save.connect(save_shared_with, sender=sender)

@receiver(post_save, sender=Note)
def save_url(sender, instance, **kwargs):
    post_save.disconnect(save_url, sender=sender)

    instance.url = slugify(instance.name)
    instance.save()

    post_save.connect(save_url, sender=sender)

m2m_changed.connect(save_shared_with, sender=Note.shared_with.through)  

# TODO model_note.py
# [ ] attachment
# [ ] implement children, parents
# [ ] board foreignkey
#     for unorganized notes
