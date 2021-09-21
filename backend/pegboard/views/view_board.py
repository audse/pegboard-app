from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone

from ..models import Board, Folder
from ..serializers import BoardSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update, get_exception_message

class BoardViewSet ( viewsets.ModelViewSet ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
    def list ( self, request ):
        return serialize_queryset( 
            serializer=self.serializer_class,
            request=request,
            identifier='boards',
            query={
                'user': request.user,
                'date_archived__isnull': True,
            }
        )

    def create ( self, request ):
        return serialize_and_create(
            serializer=self.serializer_class,
            request=request,
            identifier='board'
        )
    
    def update ( self, request, pk=None ):
        try:
            board_to_update = get_object_or_404(
                Board,
                pk=pk,
                user=request.user
            )
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=board_to_update,
                request=request,
                data=request.data,
                identifier='board'
            )
        except:
            return Response(
                data=get_exception_message(404, 'board'),
                status=404
            )

    def retrieve ( self, request, pk=None ):
        return serialize_query(
            serializer=self.serializer_class, 
            request=request,
            identifier='board',
            query={
                'pk': pk,
                'user': request.user,
                'date_archived__isnull': True
            }
        )

    @action( methods=['get'], detail=True, url_path='folder' )
    def list_by_folder ( self, request, pk ):
        try:
            current_folder = Folder.objects.get(pk=pk, user=request.user, date_archived__isnull=True)
            return serialize_queryset(
            serializer=self.serializer_class, 
            request=request,
            identifier='boards',
            query={
                'user': request.user,
                'date_archived__isnull': True,
                'folder': current_folder.id
            }
        )
        except:
            return Response(data=get_exception_message(404, 'folder'), status=404)
        
    
    @action( methods=['get'], detail=True, url_path='unsorted')
    def list_unsorted ( self, request ):
        return serialize_queryset(
            serializer=self.serializer_class,
            request=request,
            identifier='boards',
            query={
                'user': request.user,
                'folder__isnull': True,
                'date_archived__isnull': True,
            }
        )
    

    @action( methods=['get'], detail=True, url_path='archived' )
    def list_archived ( self, request ):
        return serialize_queryset(
            serializer=self.serializer_class,
            request=request,
            identifier='boards',
            query={
                'user': request.user,
                'date_archived__isnull': False,
            }
        )
    
    @action( methods=['get'], detail=True, url_path='archived' )
    def retrieve_archived ( self, request, pk ):
        return serialize_query(
            serializer=self.serializer_class,
            request=request,
            identifier='board',
            query={
                'pk': pk,
                'user': request.user,
                'date_archived__isnull': False,
            }
        )
    
    @action( methods=['put'], detail=True, url_path='archive' )
    def archive ( self, request, pk ):
        try:
            board_to_update = get_object_or_404(
                Board,
                pk=pk,
                user=request.user
            )
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=board_to_update,
                request=request,
                data={
                    'date_archived': timezone.now()
                },
                identifier='board',
            )
        except:
            return Response(
                data=get_exception_message(404, 'board'),
                status=404
            )

    @action( methods=['put'], detail=True, url_path='archive' )
    def unarchive ( self, request, pk ):
        try:
            board_to_update = get_object_or_404(
                Board,
                pk=pk,
                user=request.user
            )
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=board_to_update,
                request=request,
                data={
                    'date_archived': None,
                },
                identifier='board',
            )
        except:
            return Response(
                data=get_exception_message(404, 'board'),
                status=404
            )