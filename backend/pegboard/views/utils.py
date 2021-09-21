from __future__ import unicode_literals
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

#
# HELPER FUNCTIONS
# To assist with Django REST Framework ViewSets
# 

def get_exception_message ( status_code, identifier ):
    if status_code is 404:
        return 'This {identifier} could not be found.'
    elif status_code is 403:
        return 'You do not have permission to view this {identifier}.'
    elif status_code is 401:
        return 'You must log in to view this {identifier}.'
    elif status_code is 400:
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


# serialize_query
# RETURNS   : a singular serialized object or 404
# ARGUMENTS : <serializer:SerializerClass>, <request:Object>,
#             <identifier:String> for use in error message,
#             <query:Dict> optional filters to add to the db query e.g. { 'user': request.user }
def serialize_query ( serializer, request, identifier, query={} ):
    query_item = None
    try:
        query_item = get_object_or_404(serializer.model, **query)
    except Exception as exception:
        exception_name = type(exception).__name__
        # if exception_name is 'ObjectDoesNotExist':
            # return handle_response( HttpException(404, identifier).exception )
        return Response(
            data=get_exception_message(404, identifier),
            status=404
        )
    
        # TODO create exception cases 
        # e.g. 403 permission denied
        # they all show up as 404
    
    return Response(data=serializer(query_item, context={'request':request}).data)

# serialize_queryset
# RETURNS   : a list of serialized objects (or 404)
# ARGUMENTS : <serializer:SerializerClass>, <request:Object>
#             <identifier:String> for use in error message,
#             <query:Dict> optional filters to add to the db query e.g. { 'user': request.user }
def serialize_queryset ( serializer, request, identifier='items', query={} ):
    queryset = serializer.model.objects.all().filter(**query)
    serialized_queryset = []
    for item in queryset:
        serializer_data = serializer(item, context={'request':request})
        serialized_queryset.append(serializer_data.data)

    if len(serialized_queryset) is 0:
        return Response(
            data=get_exception_message(404, identifier),
            status=404
        )
    else:
        return Response(data=serialized_queryset)
