# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import query
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ProfileSerializer, CardSerializer, ListSerializer, BoardSerializer, ThemeSerializer

from django.contrib.auth.models import User
from .models import Card, List, Board, Theme


#
# METHODS
#

def handle_response ( data ):
    response = None
    
    if type(data) is dict and 'status_code' in data.keys() and 'message' in data.keys():
        response = Response( data['message'] )
        response.status_code = data['status_code']
    else:
        response = Response( data )

    return response

def serialize_query ( model, pk, serializer, request, identifier='item', requires_auth=True ):
    query_item = None
    try:
        if requires_auth: query_item = get_object_or_404(model, pk=pk, user=request.user)
        else: query_item = get_object_or_404(model, pk=pk)
    except:
        return { 'status_code': 404, 'message': 'The '+identifier+' is not available.' }
    return serializer(query_item, context={'request':request}).data

def serialize_query_list ( queryset, serializer, request, identifier='items' ):
    serialized_items = []
    for item in queryset:
        serializer_data = serializer(item, context={'request':request})
        serialized_items.append(serializer_data.data)

    if len(serialized_items)== 0: return { 'status_code': 404, 'message': 'No '+identifier+' are available.' }
    return serialized_items


#
# VIEWSETS
#

class ProfileViewSet ( viewsets.ModelViewSet ):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def list ( self, request ):
        return Response(serialize_query_list(
            queryset=self.queryset, 
            serializer=self.serializer_class, 
            request=request,
            identifier='profiles'
        ))

    def retrieve ( self, request, pk=None ):
        return Response( serialize_query(User, pk, self.serializer_class, request, requires_auth=False) )

class CardViewSet ( viewsets.ModelViewSet ):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list ( self, request ):
        return handle_response( serialize_query_list(
            queryset = self.queryset.filter(user=request.user), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'cards'
        ))

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = Card, 
            pk = pk, 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'card'
        ))

    @action( methods=['get'], detail=True, url_path='list' )
    def get_by_list ( self, request, pk ):
        return Response( serialize_query_list(
            queryset = self.queryset.filter(user=request.user, list__pk=pk),
            serializer = self.serializer_class,
            request = request,
            identifier = 'cards'
        ))

class ListViewSet ( viewsets.ModelViewSet ):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def list ( self, request ):
        return Response( serialize_query_list(
            queryset = self.queryset.filter(user=request.user),
            serializer = self.serializer_class,
            request = request,
            identifier = 'lists'
        ))

    def retrieve ( self, request, pk=None ):
        return Response( serialize_query(List, pk, self.serializer_class, request) )

    @action( methods=['get'], detail=True, url_path='board' )
    def get_by_board ( self, request, pk ):
        return Response( serialize_query_list(
            queryset = self.queryset.filter(user=request.user, list__pk=pk), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'lists'
        ))

class BoardViewSet ( viewsets.ModelViewSet ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def list ( self, request ):
        return Response( serialize_query_list(
            queryset = self.queryset.filter(user=request.user), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'boards'
        ))

    def retrieve ( self, request, pk=None ):
        return Response( serialize_query(Board, pk, self.serializer_class, request) )

class ThemeViewSet ( viewsets.ModelViewSet ):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    def list ( self, request ):
        return Response( serialize_query_list(
            queryset = self.queryset.filter(user=request.user), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'themes'
        ))

    def retrieve ( self, request, pk=None ):
        return Response( serialize_query(Theme, pk, self.serializer_class, request) )


#
# SERVER-SIDE PAGES
#

def home_page ( request ):
    return render( request, 'pegboard/Home.page.html' )