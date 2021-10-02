from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from django.utils import timezone

from ..models import Board
from ..serializers import BoardSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class BoardViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]
    
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
    def list(self, request):
        return serialize_queryset(
            queryset=Board.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query(
                query_object=Board.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class, 
            )
        except Exception as e:
            return Response(e, status=404)
    
    @action( methods=['get'], detail=False, url_path='unsorted')
    def list_unsorted(self, request):
        return serialize_queryset(
            queryset=Board.objects.list_unsorted(user=request.user),
            serializer=self.serializer_class,
        )

    @action( methods=['get'], detail=False, url_path='shared' )
    def list_shared_with(self, request):
        return serialize_queryset(
            queryset=Board.objects.list_shared_with(user=request.user),
            serializer=self.serializer_class,
        )
    

    @action( methods=['get'], detail=False, url_path='archived' )
    def list_archived(self, request):
        return serialize_queryset(
            queryset=Board.objects.list_archived(user=request.user),
            serializer=self.serializer_class,
        )
    
    def create(self, request):
        return serialize_and_create(
            serializer=self.serializer_class,
            request=request,
        )
    
    def update(self, request, pk=None):
        return serialize_and_update(
            serializer=self.serializer_class,
            object_to_update=Board.objects.retrieve(user=request.user, pk=pk),
            request=request,
        )

    @action( methods=['put'], detail=True, url_path='archive' )
    def archive(self, request, pk):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Board.objects.retrieve(user=request.user, pk=pk),
                data={
                    'date_archived': timezone.now()
                },
            )
        except Exception as e:
            return Response(e, status=404)

    @action( methods=['put'], detail=True, url_path='archive' )
    def unarchive(self, request, pk):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Board.objects.retrieve(user=request.user, pk=pk),
                data={
                    'date_archived': None,
                },
            )
        except Exception as e:
            return Response(e, status=404)