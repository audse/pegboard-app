from __future__ import unicode_literals
from django.db.models import query
from django.http.response import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.template.defaultfilters import slugify

from ..serializers import ProfileSerializer, CardSerializer, ListSerializer, BoardSerializer, ThemeSerializer

from django.contrib.auth.models import User
from ..models import Card, List, Board, Theme

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

