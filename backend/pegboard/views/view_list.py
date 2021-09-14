from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action

from ..models import List
from ..serializers import ListSerializer

from .utils import handle_response, serialize_queryset, serialize_query

class ListViewSet ( viewsets.ModelViewSet ):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user),
            serializer = self.serializer_class,
            request = request,
            identifier = 'lists'
        ))

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = List, 
            pk = pk,
            serializer = self.serializer_class,
            request = request
        ))

    @action( methods=['get'], detail=True, url_path='board' )
    def get_by_board ( self, request, pk ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user, list__pk=pk), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'lists'
        ))

    # TODO ListViewSet
    # @ def create
    # @ def update
    # @ def partial_update
    # @ def archive @action
