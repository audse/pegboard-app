from __future__ import unicode_literals
from django.db.models.query_utils import Q
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone

from ..models import Board, Folder
from ..serializers import BoardSerializer

from .utils import serialize_query_without_args, serialize_queryset, serialize_query, serialize_and_create, serialize_and_update, get_exception_message, serialize_queryset_without_args

class BoardViewSet ( viewsets.ModelViewSet ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
    def list ( self, request ):
        return serialize_queryset_without_args(
            queryset=Board.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def create ( self, request ):
        return serialize_and_create(
            serializer=self.serializer_class,
            request=request,
            identifier='board'
        )
    
    def update ( self, request, pk=None ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Board.objects.retrieve(user=request.user, pk=pk),
                request=request,
                data=request.data,
                identifier='board'
            )
        except Exception as e:
            return Response(e, status=404)

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query_without_args(
                query_object=Board.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class, 
            )
        except Exception as e:
            return Response(e, status=404)
    
    @action( methods=['get'], detail=True, url_path='shared' )
    def list_by_shared_with ( self, request ):
        return serialize_queryset_without_args(
            queryset=Board.objects.list_shared_with(user=request.user),
            serializer=self.serializer_class,
        )

    @action( methods=['get'], detail=True, url_path='folder' )
    def list_by_folder ( self, request, pk ):
        try:
            current_folder = Folder.objects.retrieve(pk=pk, user=request.user)
            return serialize_queryset_without_args(
                queryset=Board.objects.list_by_folder(user=request.user, folder=current_folder),
                serializer=self.serializer_class,
            )
        except:
            return Response(data=get_exception_message(404, 'folder'), status=404)
        
    
    @action( methods=['get'], detail=True, url_path='unsorted')
    def list_unsorted ( self, request ):
        return serialize_queryset_without_args(
            queryset=Board.objects.list_unsorted(user=request.user),
            serializer=self.serializer_class,
        )
    

    @action( methods=['get'], detail=True, url_path='archived' )
    def list_archived ( self, request ):
        return serialize_queryset_without_args(
            queryset=Board.objects.list_archived(user=request.user),
            serializer=self.serializer_class,
        )
    
    @action( methods=['get'], detail=True, url_path='archived' )
    def retrieve_archived ( self, request, pk ):
        try:
            return serialize_query_without_args(
                query_object=Board.objects.retrieve_archived(user=request.user, pk=pk),
                serializer=self.serializer_class,
            )
        except Exception as e:
            return Response(e, status=404)
    
    @action( methods=['put'], detail=True, url_path='archive' )
    def archive ( self, request, pk ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Board.objects.retrieve(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': timezone.now()
                },
                identifier='board',
            )
        except Exception as e:
            return Response(e, status=404)

    @action( methods=['put'], detail=True, url_path='archive' )
    def unarchive ( self, request, pk ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Board.objects.retrieve_archived(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': None,
                },
                identifier='board',
            )
        except Exception as e:
            return Response(e, status=404)