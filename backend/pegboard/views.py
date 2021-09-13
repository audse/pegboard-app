# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import query
from django.shortcuts import render, get_object_or_404

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ProfileSerializer, CardSerializer, ListSerializer, BoardSerializer, ThemeSerializer

from .models import Card, List, Board, Theme


#
# METHODS
#

def serialize_query ( query_class, pk, serializer, request, requires_auth=True ):
    query_item = None
    if requires_auth: query_item = get_object_or_404(query_class, pk=pk, user=request.user)
    else: query_item = get_object_or_404(query_class, pk=pk)
    return serializer(query_item, context={'request':request}).data

def serialize_query_list ( query_items, serializer, request ):
    serialized_items = []
    for item in query_items:
        serializer_data = serializer(item, context={'request':request})
        serialized_items.append(serializer_data.data)
    return serialized_items


#
# VIEWSETS
# 

class CardViewSet ( viewsets.ModelViewSet ):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list ( self, request ):
        return Response(serialize_query_list(
            self.queryset.filter(user=request.user), 
            self.serializer_class, 
            request
        ))

    def retrieve ( self, request, pk=None ):
        return Response( serialize_query(Card, pk, self.serializer_class, request) )

    @action( methods=['get'], detail=True, url_path='list' )
    def get_by_list ( self, request, pk ):
        return Response(serialize_query_list(
            self.queryset.filter(user=request.user, list__pk=pk),
            self.serializer_class,
            request
        ))

class ListViewSet ( viewsets.ModelViewSet ):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def list ( self, request ):
        return Response( serialize_query_list(
            self.queryset.filter(user=request.user),
            self.serializer_class,
            request
        ))

    def retrieve ( self, request, pk=None ):
        return Response( serialize_query(List, pk, self.serializer_class, request) )

    @action( methods=['get'], detail=True, url_path='board' )
    def get_by_board ( self, request, pk ):
        return Response( serialize_query_list(
            self.queryset.filter(user=request.user, list__pk=pk), 
            self.serializer_class, 
            request
        ))

class BoardViewSet ( viewsets.ModelViewSet ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def list ( self, request ):
        return Response( serialize_query_list(
            self.queryset.filter(user=request.user), 
            self.serializer_class, 
            request
        ))

    def retrieve ( self, request, pk=None ):
        return Response( serialize_query(Board, pk, self.serializer_class, request) )

class ThemeViewSet ( viewsets.ModelViewSet ):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    def list ( self, request ):
        return Response( serialize_query_list(
            self.queryset.filter(user=request.user), 
            self.serializer_class, 
            request
        ))

    def retrieve ( self, request, pk=None ):
        return Response( serialize_query(Theme, pk, self.serializer_class, request) )


#
# SERVER-SIDE PAGES
#

def home_page ( request ):
    return render( request, 'pegboard/Home.page.html' )