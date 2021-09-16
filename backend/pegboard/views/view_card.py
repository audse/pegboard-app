from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action

from ..models import Card, List
from ..serializers import CardSerializer

from .utils import HttpException, handle_response, serialize_queryset, serialize_query

class CardViewSet ( viewsets.ModelViewSet ):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list ( self, request ):
        return handle_response(serialize_queryset(
            serializer = self.serializer_class, 
            request = request,
            identifier = 'cards',
            query = {
                'user': request.user,
                'date_archived__isnull': True
            }
        ))
    
    # TESTME <CardViewSet> `create`
    def create ( self, request ):
        serialized_request = self.serializer_class(data=request.data)
        if serialized_request.is_valid():
            # TODO switch to args function
            serialized_request.save(user=request.user)
            return handle_response(serialized_request.validated_data) 
        else:
            return handle_response({
                'status_code': 500,
                'message': 'A card could not be created at this time.'
            })

    def retrieve ( self, request, pk=None ):
        return handle_response(serialize_query(
            serializer = self.serializer_class, 
            request = request,
            identifier = 'card',
            query = {
                'pk': pk,
                'user': request.user, # TODO replace `user` query with `shared_with`
                'date_archived__isnull': True
            }
        ))

    @action( methods=['get'], detail=True, url_path='list' )
    def get_by_list ( self, request, pk ):
        current_list = None
        try: current_list = List.objects.get(pk=pk, user=request.user, date_archived__isnull=True)
        except: return handle_response( HttpException(404, 'list').exception )

        return handle_response(serialize_queryset(
            serializer = self.serializer_class,
            request = request,
            identifier = 'cards',
            query = {
                'user': request.user,
                'list': current_list,
                'date_archived__isnull': True,
            }
        ))
    
    # TODO CardViewSet
    # [ ] def create
    # [ ] def update
    # [ ] def partial_update
    # [ ] def @action archive
    # [ ] def @action get_unorganized
    #     no list specified
    # [ ] def @action get_archived