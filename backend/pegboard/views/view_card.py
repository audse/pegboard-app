from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action

from ..models import Card
from ..serializers import CardSerializer

from .utils import handle_response, serialize_queryset, serialize_query

class CardViewSet ( viewsets.ModelViewSet ):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'cards'
        ))
    
    def create ( self, request ):
        pass

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = Card, 
            pk = pk, 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'card'
        ))

    @action( methods=['get'], detail=True, url_path='list' )
    def get_by_list ( self, request, pk ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user, list__pk=pk),
            serializer = self.serializer_class,
            request = request,
            identifier = 'cards'
        ))
    
    # TODO CardViewSet
    # @ def create
    # @ def update
    # @ def partial_update
    # @ def archive @action