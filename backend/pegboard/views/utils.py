from __future__ import unicode_literals
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

#
# HELPER FUNCTIONS
# To assist with Django REST Framework ViewSets
# 
# TODO views.py
# @ def create_response
#

''' class Error
PROPS : <status_code:Number>,
        <identifier:String> a semantic name to be used in the error code
USE   : call Error(status_code, identifier).exception to return:
        { 'status_code' : status_code,
          'message' : <a message from status_code> }
'''
class Error:
    def __init__ ( self, status_code, identifier='item' ):
        self.status_code = status_code
        self.identifier = identifier
        self.exception = self.create_exception()
    
    def create_exception ( self ):
        exception = {
            'status_code': self.status_code,
            'message': 'An internal error occurred, please try again later.'
        },

        if self.status_code is 404:
            exception['message'] = 'This {identifier} could not be found.'
        elif self.status_code is 403:
            exception['message'] = 'You do not have permission to view this {identifier}.'
        elif self.status_code is 401:
            exception['message'] = 'You must log in to view this {identifier}.'

        return exception

''' handle_response
RETURNS   : an API response containing the serialized data (or an exception)
ARGUMENTS : <data:Object||List> a serialized object or list of objects
'''
def handle_response ( data ):
    response = None
    
    keys = data.keys() if type(data) is dict else []
    if type(data) is dict and 'status_code' in keys and 'message' in keys:
        response = Response( data['message'] )
        response.status_code = data['status_code']
    else:
        response = Response( data )

    return response


# serialize_and_create
# RETURNS    : a singular serialized object or <500:BadRequest>
# ARGUMENTS : <serializer:SerializerClass>, <request:Object> with <request.data>,
#            <identifier:String> for use in error message
def serialize_and_create ( serializer, request, identifier ):
    serialized_request = serializer.model.create(data=request.data)
    if serialized_request.is_valid():
        serialized_request.save(user=request.user)
        return handle_response(serialized_request.validated_data)
    else:
        return handle_response({
            'status_code': 500,
            'message': 'A board could not be created at this time.'
        })

''' serialize_query
RETURNS   : a singular serialized object or 404
ARGUMENTS : <model:ModelClass>, <pk:Number>, <serializer:SerializerClass>,
            <request:Object>, <requires_auth:Boolean>,
            <identifier:String> for use in error message
'''
def serialize_query ( model, pk, serializer, request, identifier='item', requires_auth=True ):
    query_item = None
    try:
        if requires_auth: query_item = get_object_or_404(model, pk=pk, user=request.user)
        else: query_item = get_object_or_404(model, pk=pk)
    except:
        return { 'status_code': 404, 'message': 'This '+identifier+' is not available.' }
    return serializer(query_item, context={'request':request}).data

def serialize_query_with_args ( serializer, request, identifier, **filter ):
    query_item = None
    try:
        query_item = get_object_or_404(serializer.model, **filter)
    except Exception as exception:
        exception_name = type(exception).__name__
        if exception_name is 'ObjectDoesNotExist':
            return Error(404, identifier).exception
    
        # TODO create exception cases 
        # e.g. 403 permission denied
        # they all show up as 404
    
    return serializer(query_item, context={'request':request}).data



''' serialize_queryset
RETURNS   : a list of serialized objects (or 404)
ARGUMENTS : <queryset:ModelQuery>, <serializer:SerializerClass>, <request:Object>
            <identifier:String> for use in error message
'''
def serialize_queryset ( queryset, serializer, request, identifier='items' ):
    serialized_items = []
    for item in queryset:
        serializer_data = serializer(item, context={'request':request})
        serialized_items.append(serializer_data.data)

    if len(serialized_items) == 0: return { 'status_code': 404, 'message': 'No '+identifier+' are available.' }
    return serialized_items

def serialize_queryset_with_args ( serializer, request, identifier='items', **filter ):
    queryset = serializer.model.objects.all().filter(**filter)
    serialized_queryset = []
    for item in queryset:
        serializer_data = serializer(item, context={'request':request})
        serialized_queryset.append(serializer_data.data)

    if len(serialized_queryset) == 0: return Error(404, identifier)
    else: return serialized_queryset
