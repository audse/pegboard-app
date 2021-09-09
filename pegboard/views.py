# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from .models import Card

# Create your views here.

def index ( request ):
    return HttpResponse('You are home.')

def view_card ( request, card_id, card_slug ):
    current_card = Card.objects.get(pk=card_id)
    return HttpResponse('You are viewing your card: '+current_card.url)

def add_card ( request ):
    return HttpResponse('You are adding a card.')