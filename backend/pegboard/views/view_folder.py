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
        return serialize_queryset(
            queryset=Folder.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query(
                query_object=Folder.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class,
            )
        except Exception as e:
            return Response(str(e))
            # return Response(str(e), status=404)

    @action( methods=['get'], detail=False, url_path='archived' )
    def list_archived ( self, request ):
        return serialize_queryset(
            queryset=Folder.objects.list_archived(user=request.user),
            serializer=self.serializer_class,
        )

    def create ( self, request ):
        return serialize_and_create(
            serializer=self.serializer_class,
            data={
                'user': request.user.pk,
                **request.data
            }
        )
    
    def update ( self, request, pk=None ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Folder.objects.retrieve(user=request.user, pk=pk),
                data=request.data,
            )
        except Exception as e:
            return Response(str(e))
    
    @action( methods=['put'], detail=True, url_path='archive' )
    def archive ( self, request, pk ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Folder.objects.retrieve(user=request.user, pk=pk),
                data={
                    'date_archived': timezone.now()
                },
            )
        except Exception as e:
            return Response(str(e), status=404)

    @action( methods=['put'], detail=True, url_path='archive' )
    def unarchive ( self, request, pk ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Folder.objects.retrieve(user=request.user, pk=pk),
                data={
                    'date_archived': None,
                },
            )
        except Exception as e:
            return Response(str(e), status=404)