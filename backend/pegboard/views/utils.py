from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response


def serialize_and_create (serializer, data):
    serialized_request = serializer(data=data)
    if serialized_request.is_valid():
        serialized_request.save()
        return Response(data=serialized_request.data)
    else:
        return Response(serialized_request.errors, status=400)

def serialize_and_update ( serializer, object_to_update, data ):
    serialized_request = serializer(object_to_update, data=data, partial=True)
    if serialized_request.is_valid():
        serialized_request.save()
        return Response(data=serialized_request.data)
    else:
        return Response(serialized_request.errors, status=400)
        
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