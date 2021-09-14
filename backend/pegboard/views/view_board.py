from __future__ import unicode_literals
from rest_framework import viewsets

from ..models import Board
from ..serializers import BoardSerializer

from .utils import handle_response, serialize_queryset, serialize_query

class BoardViewSet ( viewsets.ModelViewSet ):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'boards'
        ))

    def create ( self, request ):

        serialized_request = self.serializer_class(data=request.data)
        if serialized_request.is_valid():
            serialized_request.save(user=request.user)
            return handle_response(serialized_request.validated_data)
        else:
            return handle_response({
                'status_code': 500,
                'message': 'A board could not be created at this time.'
            })

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = Board, 
            pk = pk, 
            serializer = self.serializer_class, 
            request = request
        ))
    
    # TODO BoardViewSet
    # @ def update
    # @ def partial_update
    # @ def archive @action
