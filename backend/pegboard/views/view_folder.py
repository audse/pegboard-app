from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from django.utils import timezone

from ..models import Folder
from ..serializers import FolderSerializer

from .utils import serialize_query, serialize_queryset, serialize_and_create, serialize_and_update

class FolderViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]

    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def list ( self, request ):
        try:
            return serialize_queryset(
                queryset=Folder.objects.list(user=request.user),
                serializer=self.serializer_class,
            )
        except Exception as e:
            print('Error listing folders:', e)
            return Response(str(e))

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query(
                query_object=Folder.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class,
            )
        except Exception as e:
            print('Error retrieving folder:', e)
            return Response(str(e))

    def create ( self, request ):
        return serialize_and_create(
            serializer=self.serializer_class,
            request=request,
        )
    
    def update ( self, request, pk=None ):
        return serialize_and_update(
            serializer=self.serializer_class,
            object_to_update=Folder.objects.retrieve(user=request.user, pk=pk),
            request=request,
        )
    
    @action( methods=['put'], detail=True, url_path='archive' )
    def archive ( self, request, pk ):
        return self.update(request, pk)

    @action( methods=['put'], detail=True, url_path='archive' )
    def unarchive ( self, request, pk ):
        return self.update(request, pk)