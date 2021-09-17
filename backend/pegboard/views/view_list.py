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
                get_object_or_404(Board, pk=request.data['board'])
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
        pass

    def retrieve ( self, request, pk=None ):
        return serialize_query(
            serializer=self.serializer_class,
            request=request,
            query={
                'pk': pk,
                'user': request.user,
                'date_archived__isnull': True,
            }
        )

    @action( methods=['get'], detail=True, url_path='board' )
    def get_by_board ( self, request, pk ):
        return serialize_queryset(
            serializer=self.serializer_class, 
            request=request,
            identifier='lists',
            query={
                'user': request.user,
                'date_archived__isnull': True,
                'list__pk': pk,
            }
        )

    # TODO ListViewSet
    # [x] def create
    # [ ] def update
    # [ ] def archive @action
