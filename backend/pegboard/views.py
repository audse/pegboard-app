# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404

from .models import Card, List, Board
from .forms import CardForm, ListForm, BoardForm

# Pages

def home_page ( request ):
    return render( request, 'pegboard/Home.page.html' )

def add_card_page ( request ):
    return render( request, 'pegboard/AddCard.page.html' )

def add_list_page ( request ):
    return render( request, 'pegboard/AddList.page.html' )

def add_board_page ( request ):
    form = BoardForm()
    return render( request, 'pegboard/AddBoard.page.html', { 'form': form } )

# API

def view_card ( request, card_id, card_slug ):
    current_card = get_object_or_404(Card, pk=card_id)
    return render( request, 'pegboard/Card.html', { 'card': current_card } )

def view_list ( request, list_id, list_slug ):
    current_list = get_object_or_404(List, pk=list_id)
    return render( request, 'pegboard/List.html', { 'list': current_list } )

def view_board ( request, board_id, board_slug ):
    current_board = get_object_or_404(Board, pk=board_id)
    return render( request, 'pegboard/Board.html', { 'board': current_board } )