# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CardSerializer, ListSerializer, BoardSerializer

from .models import Card, List, Board
from .forms import CardForm, ListForm, BoardForm

class CardViewSet ( viewsets.ModelViewSet ):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @action( methods=['get'], detail=True, url_path='list', name='get_by_list' )
    def get_by_list ( self, request, pk ):

        cards = Card.objects.all().filter(list__pk = pk)
        serialized_cards = []

        for card in cards:
            serializer = CardSerializer(card, context={'request':request})
            serialized_cards.append(serializer.data)

        return Response(serialized_cards)

class ListViewSet ( viewsets.ModelViewSet ):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    @action( methods=['get'], detail=True, url_path='board', name='get_by_board' )
    def get_by_board ( self, request, pk ):

        lists = List.objects.all().filter(list__pk = pk)
        serialized_lists = []

        for each_list in lists:
            serializer = ListSerializer(each_list, context={'request':request})
            serialized_lists.append(serializer.data)

        return Response(serialized_lists)

class BoardViewSet ( viewsets.ModelViewSet ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

# Pages

def home_page ( request ):
    return render( request, 'pegboard/Home.page.html' )

# def add_card_page ( request ):
#     return render( request, 'pegboard/AddCard.page.html' )

# def add_list_page ( request ):
#     return render( request, 'pegboard/AddList.page.html' )

# def add_board_page ( request ):
#     form = BoardForm()
#     return render( request, 'pegboard/AddBoard.page.html', { 'form': form } )

# API

# def view_card ( request, card_id, card_slug ):
#     current_card = get_object_or_404(Card, pk=card_id)
#     return render( request, 'pegboard/Card.html', { 'card': current_card } )

# def view_list ( request, list_id, list_slug ):
#     current_list = get_object_or_404(List, pk=list_id)
#     return render( request, 'pegboard/List.html', { 'list': current_list } )

# def view_board ( request, board_id, board_slug ):
#     current_board = get_object_or_404(Board, pk=board_id)
#     return render( request, 'pegboard/Board.html', { 'board': current_board } )