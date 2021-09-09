# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404

from .models import Card, List, Board

# Pages

def home_page ( request ):
    return render( request, 'pegboard/Home.page.html' )

def add_card ( request ):
    return render( request, 'pegboard/AddCard.page.html' )

def add_list ( request ):
    return render( request, 'pegboard/AddList.page.html' )

def add_board ( request ):
    return render( request, 'pegboard/AddBoard.page.html' )

# API

def view_card ( request, card_id, card_slug ):
    current_card = get_object_or_404(Card, pk=card_id)
    return render( request, { 'card': current_card } )
