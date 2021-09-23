from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.utils import timezone

from ..models import Board, Folder
from ..serializers import BoardSerializer, PageSerializer, NoteSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class BoardViewSet ( viewsets.ModelViewSet ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def validate_board(self, request):
        if 'folder' in request.data.keys():
            try:
                get_object_or_404(Folder, pk=request.data['folder'], user=request.user)
            except:
                return False
        return True
    
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
    
    @action(detail=True, url_path='pages')
    def list_children(self, request, pk):
        try:
            return serialize_queryset(
                queryset=Board.objects.list_children(user=request.user, pk=pk),
                serializer=PageSerializer
            )
        except Exception as e:
            return Response(e, status=404)
    
    @action(detail=True, url_path='page')
    def retrieve_child(self, request, board_pk=None, page_pk=None):
        try:
            return serialize_queryset(
                queryset=Board.objects.retrieve_child(
                    user=request.user,
                    board_pk=board_pk,
                    page_pk=page_pk
                ),
                serializer=PageSerializer
            )
        except Exception as e:
            return Response(e, status=404)
    
    @action(detail=True, url_path='pages/archived')
    def list_archived_children(self, request, pk):
        try:
            return serialize_queryset(
                queryset=Board.objects.list_archived_children(request.user, pk),
                serializer=PageSerializer
            )
        except Exception as e:
            return Response(e, status=404)

    @action(detail=True, url_path='notes')
    def list_grandchildren(self, request, pk=None):
        try:
            pk_list = pk.split('-')
            board_pk = pk_list[0]
            page_pk = pk_list[1]
            return serialize_queryset(
                queryset=Board.objects.list_grandchildren(
                    user=request.user,
                    board_pk=board_pk,
                    page_pk=page_pk
                ),
                serializer=NoteSerializer
            )
        except Exception as e:
            print('\n\nCURRENT ERROR', e, '\n\n')
            return Response(e, status=404)
    
    @action(detail=True, url_path='note')
    def retrieve_grandchild(self, request, pk):
        try:
            pk_list = pk.split('-')
            board_pk = pk_list[0]
            page_pk = pk_list[1]
            note_pk = pk_list[2]
            return serialize_queryset(
                queryset=Board.objects.retrieve_grandchild(
                    user=request.user,
                    board_pk=board_pk,
                    page_pk=page_pk,
                    note_pk=note_pk
                ),
                serializer=PageSerializer
            )
        except Exception as e:
            return Response(e, status=404)

    @action(detail=True, url_path='notes/archived')
    def list_archived_grandchildren(self, request, pk):
        try:
            pk_list = pk.split('-')
            board_pk = pk_list[0]
            page_pk = pk_list[1]
            return serialize_queryset(
                queryset=Board.objects.list_archived_grandchildren(
                    user=request.user,
                    board_pk=board_pk,
                    page_pk=page_pk
                ),
                serializer=NoteSerializer
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
        if self.validate_board(request):
            return serialize_and_create(
                serializer=self.serializer_class,
                data={
                    'user': request.user.pk,
                    **request.data
                }
            )
        else:
            return Response('An error validating the data occurred.', status=500)
    
    def update(self, request, pk=None):
        if self.validate_board(request):
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
        else:
            return Response('An error validating the data occurred.', status=500)

    @action( methods=['put'], detail=True, url_path='archive' )
    def archive(self, request, pk):
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
    def unarchive(self, request, pk):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Board.objects.retrieve(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': None,
                },
                identifier='board',
            )
        except Exception as e:
            return Response(e, status=404)