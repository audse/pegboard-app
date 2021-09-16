from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Card, List
from ..serializers import CardSerializer

from .utils import get_exception_message, serialize_and_create, serialize_queryset, serialize_query

class CardViewSet ( viewsets.ModelViewSet ):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def validate_card ( self, request ):
        valid = True
        if 'list' in request.data.keys():
            try:
                current_list = get_object_or_404(List, user=request.user, pk=request.data['list'])
                # TODO replace `user` with `shared_with`
            except:
                return False
        return valid


    def list ( self, request ):
        return serialize_queryset(
            serializer = self.serializer_class, 
            request = request,
            identifier = 'cards',
            query = {
                'user': request.user,
                'date_archived__isnull': True
            }
        )

    def create ( self, request ):
        valid = self.validate_card(request)
        
        if valid:
            return serialize_and_create(
                serializer=self.serializer_class,
                request=request,
                identifier='card'
            )
        else:
            return Response(data=get_exception_message(400, 'card'), status=400)
    
    # def update ( self, request ):
    #     valid = True
    #     if 'list' in request.data.keys()

    def retrieve ( self, request, pk=None ):
        return serialize_query(
            serializer=self.serializer_class, 
            request=request,
            identifier='card',
            query={
                'pk': pk,
                'user': request.user, # TODO replace `user` query with `shared_with`
                'date_archived__isnull': True
            }
        )

    @action( methods=['get'], detail=True, url_path='list' )
    def get_by_list ( self, request, pk ):
        current_list = None
        try:
            current_list = List.objects.get(pk=pk, user=request.user, date_archived__isnull=True)
        except:
            return Response(data=get_exception_message(404, 'list'), status=404)

        return serialize_queryset(
            serializer=self.serializer_class,
            request=request,
            identifier='cards',
            query={
                'user': request.user,
                'list': current_list,
                'date_archived__isnull': True,
            }
        )
    
    # TODO CardViewSet
    # [x] def create
    # [ ] def update
    # [ ] def partial_update
    # [ ] def @action archive
    # [ ] def @action get_unorganized
    #     no list specified
    # [ ] def @action get_archived