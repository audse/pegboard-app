from __future__ import unicode_literals
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

#
# HELPER FUNCTIONS
# To assist with Django REST Framework ViewSets
# 

#FIXME
# [x] merge serialize_x and serialize_x_with_args
# [ ] update views to use new serialize method
# [x] reformat function comments

# class HttpException
# PROPS : <status_code:Number>,
#         <identifier:String> a semantic name to be used in the error code
# USE   : call HttpException(status_code, identifier).exception to return:
#        { 'status_code' : status_code,
#           'message' : <a message from status_code> }
class HttpException:

    def __init__ ( self, status_code, identifier='item' ):
        self.status_code = status_code
        self.identifier = identifier
        self.exception = {
            'status_code': self.status_code,
            'message': self.create_message(status_code)
        }
    
    def create_message ( self, status_code ):

        if status_code is 404:
            return 'This {identifier} could not be found.'
        elif status_code is 403:
            return 'You do not have permission to view this {identifier}.'
        elif status_code is 401:
            return 'You must log in to view this {identifier}.'
        else: return 'An internal error occurred, please try again later.'

# handle_response
# RETURNS   : an API response containing the serialized data (or an exception)
# ARGUMENTS : <data:Object||List> a serialized object or list of objects
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
        return serialized_request.validated_data
    else:
        return HttpException(500, identifier).exception

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
        return HttpException(404, identifier).exception
    
        # TODO create exception cases 
        # e.g. 403 permission denied
        # they all show up as 404
    
    return serializer(query_item, context={'request':request}).data

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

    if len(serialized_queryset) is 0: return HttpException(404, identifier).exception
    else: return serialized_queryset
