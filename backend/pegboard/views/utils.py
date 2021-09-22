from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

#
# HELPER FUNCTIONS
# To assist with Django REST Framework ViewSets
# 

def get_exception_message ( status_code, identifier ):
    if status_code == 404:
        return 'This {identifier} could not be found.'
    elif status_code == 403:
        return 'You do not have permission to view this {identifier}.'
    elif status_code == 401:
        return 'You must log in to view this {identifier}.'
    elif status_code == 400:
        return 'There was a problem with the {identifier} data. Please fix any issues and try again.'
    else: return 'An internal error with this {identifier} occurred, please try again later.'


# serialize_and_create
# RETURNS    : a singular serialized object or <500:BadRequest>
# ARGUMENTS : <serializer:SerializerClass>, <request:Object> with <request.data>,
#            <identifier:String> for use in error message
def serialize_and_create ( serializer, request, identifier ):
    serialized_request = serializer(data=request.data, context={'request':request})
    if serialized_request.is_valid():
        serialized_request.save()
        return Response(data=serialized_request.data)
    else:
        return Response(
            data=get_exception_message(400, identifier),
            status=400
        )

def serialize_and_update ( serializer, object_to_update, request, data , identifier):
    serialized_request = serializer(object_to_update, data=data, partial=True, context={'request':request})
    if serialized_request.is_valid():
        serialized_request.save()
        return Response(data=serialized_request.data)
    else:
        return Response(
            data=get_exception_message(400, identifier),
            status=400
        )
        
def serialize_query(query_object, serializer):
    return Response(data=serializer(query_object).data)

def serialize_queryset(queryset, serializer):
    try:
        serialized_queryset = []
        for item in queryset:
            serializer_data = serializer(item)
            serialized_queryset.append(serializer_data.data)
        
        if len(serialized_queryset) == 0:
            raise FileNotFoundError

        return Response(data=serialized_queryset)
    except Exception as e:
        return Response(e, status=404)