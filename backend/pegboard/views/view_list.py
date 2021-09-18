from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import List, Board
from ..serializers import ListSerializer

from .utils import get_exception_message, serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class ListViewSet ( viewsets.ModelViewSet ):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def validate_list ( self, request ):
        if 'board' in request.data.keys():
            try:
                get_object_or_404(Board, pk=request.data['board'], user=request.user)
            except:
                return False
        return True

    def list ( self, request ):
        return serialize_queryset(
            serializer=self.serializer_class,
            request=request,
            identifier='lists',
            query={
                'user': request.user,
                'date_archived__isnull': True,
            }
        )

    def create ( self, request ):
        if self.validate_list(request):
            return serialize_and_create(
                serializer=self.serializer_class,
                request=request,
                identifier='lists',
            )
        else:
            return Response(
                data=get_exception_message(404, 'board'),
                status=404
            )
    
    def update ( self, request, pk=None ):
        if self.validate_list(request):

            list_to_update = None
            try:
                list_to_update = get_object_or_404(List, pk=pk, user=request.user)
            except:
                return Response(
                    data=get_exception_message(404, 'list'),
                    status=404
                )
            
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=list_to_update,
                request=request,
                identifier='list'
            )
        else:
            return Response(
                data=get_exception_message(400, 'list'),
                status=400
            )

    def retrieve ( self, request, pk=None ):
        return serialize_query(
            serializer=self.serializer_class,
            request=request,
            identifier='list',
            query={
                'pk': pk,
                'user': request.user,
                'date_archived__isnull': True,
            }
        )

    @action( methods=['get'], detail=True, url_path='board' )
    def get_by_board ( self, request, pk ):
        current_board = None
        try:
            current_board = Board.objects.get(pk=pk, user=request.user, date_archived__isnull=True)
        except:
            return Response(data=get_exception_message(404, 'list'), status=404)
        return serialize_queryset(
            serializer=self.serializer_class, 
            request=request,
            identifier='lists',
            query={
                'user': request.user,
                'date_archived__isnull': True,
                'board': current_board.id
            }
        )

    # TODO ListViewSet
    # [ ] def @action archive 
    # [ ] def @action unarchive
    # [ ] def @action list_unsorted
    # [ ] def @action list_archived
    # [ ] def @action retrieve_archived
