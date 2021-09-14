# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import query
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.template.defaultfilters import slugify

from .serializers import ProfileSerializer, CardSerializer, ListSerializer, BoardSerializer, ThemeSerializer

from django.contrib.auth.models import User
from .models import Card, List, Board, Theme


#
# HELPER FUNCTIONS
# To assist with Django REST Framework ViewSets
# 
# TODO views.py
# @ def create_response
#

'''
handle_response
RETURNS     an API response containing the serialized data (or an error)
ARGUMENTS   <data> a serialized object or list of objects
'''
def handle_response ( data ):
    response = None
    
    if type(data) is dict and 'status_code' in data.keys() and 'message' in data.keys():
        response = Response( data['message'] )
        response.status_code = data['status_code']
    else:
        response = Response( data )

    return response


'''
serialize_query
RETURNS     a singular serialized object (or a 404 error)
ARGUMENTS   <model:ModelClass>, <pk:Number>, <serializer:SerializerClass>,
            <request:Object>, <requires_auth:Boolean>,
            <identifier:String> for use in error message
'''
def serialize_query ( model, pk, serializer, request, identifier='item', requires_auth=True ):
    query_item = None
    try:
        if requires_auth: query_item = get_object_or_404(model, pk=pk, user=request.user)
        else: query_item = get_object_or_404(model, pk=pk)
    except:
        return { 'status_code': 404, 'message': 'The '+identifier+' is not available.' }
    return serializer(query_item, context={'request':request}).data


'''
serialize_queryset
RETURNS     a list of serialized objects (or a 404 error)
ARGUMENTS   <queryset:ModelQuery>, <serializer:SerializerClass>, <request:Object>
            <identifier:String> for use in error message
'''
def serialize_queryset ( queryset, serializer, request, identifier='items' ):
    serialized_items = []
    for item in queryset:
        serializer_data = serializer(item, context={'request':request})
        serialized_items.append(serializer_data.data)

    if len(serialized_items) == 0: return { 'status_code': 404, 'message': 'No '+identifier+' are available.' }
    return serialized_items


#
# VIEWSETS
#

class ProfileViewSet ( viewsets.ModelViewSet ):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset=self.queryset, 
            serializer=self.serializer_class, 
            request=request,
            identifier='profiles'
        ))

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = User, 
            pk = pk, 
            serializer = self.serializer_class, 
            request = request, 
            identifier = 'profile', 
            requires_auth=False
        ))
    
    # TODO ProfileViewSet
    # @ def create
    # @ def update
    # @ def partial_update


class CardViewSet ( viewsets.ModelViewSet ):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'cards'
        ))
    
    def create ( self, request ):
        pass

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
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user, list__pk=pk),
            serializer = self.serializer_class,
            request = request,
            identifier = 'cards'
        ))
    
    # TODO CardViewSet
    # @ def create
    # @ def update
    # @ def partial_update
    # @ def archive @action

class ListViewSet ( viewsets.ModelViewSet ):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user),
            serializer = self.serializer_class,
            request = request,
            identifier = 'lists'
        ))

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = List, 
            pk = pk,
            serializer = self.serializer_class,
            request = request
        ))

    @action( methods=['get'], detail=True, url_path='board' )
    def get_by_board ( self, request, pk ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user, list__pk=pk), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'lists'
        ))

    # TODO ListViewSet
    # @ def create
    # @ def update
    # @ def partial_update
    # @ def archive @action


class BoardViewSet ( viewsets.ModelViewSet ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'boards'
        ))

    def create ( self, request ):

        serialized_request = self.serializer_class(data=request.data)
        if serialized_request.is_valid():
            serialized_request.save(user=request.user)
            return handle_response(serialized_request.validated_data)
        else:
            return handle_response({
                'status_code': 500,
                'message': 'A board could not be created at this time.'
            })

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = Board, 
            pk = pk, 
            serializer = self.serializer_class, 
            request = request
        ))
    
    # TODO BoardViewSet
    # @ def update
    # @ def partial_update
    # @ def archive @action


class ThemeViewSet ( viewsets.ModelViewSet ):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'themes'
        ))

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = Theme, 
            pk = pk, 
            serializer = self.serializer_class, 
            request = request
        ))
    
    # TODO ThemeViewSet
    # @ def create
    # @ def update
    # @ def partial_update
    # @ def archive @action


#
# SERVER-SIDE PAGES
#

def home_page ( request ):
    return render( request, 'pegboard/Home.page.html' )