from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from ..models import Board, Page, Note, Color

def validate_foreign_keys (user, data):

    # Check to make sure that every foreign key entered
    # links to a real object.
    # If not, raises exception (built-in) so use with try/catch

    foreign_keys = {
        'board': Board,
        'page': Page,
        'note': Note,
        'color': Color
    }

    validated_keys = {}
    request_keys = data.keys()

    for key in foreign_keys.keys():
        if key in request_keys and data[key] is not None:
            foreign_keys[key].objects.retrieve(pk=data[key], user=user)
            validated_keys[key] = data[key]

    return validated_keys

def serialize_and_create (serializer, request):
    try:
        validated_foreign_keys = validate_foreign_keys(request.user, request.data)
        serialized_request = serializer(
            data={
                'user': request.user.id,
                **request.data,
                **validated_foreign_keys
            }
        )

        if serialized_request.is_valid():
            serialized_request.save(user=request.user)
            return Response(data=serialized_request.data)

        else:
            print('Error serializing request:', serialized_request.errors)
            return Response(serialized_request.errors, status=400)

    except Exception as e:
        print('Error creating object:', e)
        return Response(str(e), status=500)

def serialize_and_update(serializer, object_to_update, request):
    try:
        validated_foreign_keys = validate_foreign_keys(request.user, request.data)
        serialized_request = serializer(
            object_to_update,
            partial=True,
            data={
                **request.data,
                **validated_foreign_keys
            }
        )

        if serialized_request.is_valid():
            serialized_request.save()
            return Response(data=serialized_request.data)

        else:
            print('Error serializing request:', serialized_request.errors)
            return Response(serialized_request.errors, status=400)

    except Exception as e:
        print('Error updating request:', e)
        return Response(str(e), status=500)
        
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
        return Response(status=404)