from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Page, Board
from ..serializers import PageSerializer

from .utils import get_exception_message, serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class PageViewSet ( viewsets.ModelViewSet ):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def validate_page ( self, request ):
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
            identifier='pages',
            query={
                'user': request.user,
                'date_archived__isnull': True,
            }
        )

    def create ( self, request ):
        if self.validate_page(request):
            return serialize_and_create(
                serializer=self.serializer_class,
                request=request,
                identifier='pages',
            )
        else:
            return Response(
                data=get_exception_message(404, 'board'),
                status=404
            )
    
    def update ( self, request, pk=None ):
        if self.validate_page(request):

            page_to_update = None
            try:
                page_to_update = get_object_or_404(Page, pk=pk, user=request.user)
            except:
                return Response(
                    data=get_exception_message(404, 'page'),
                    status=404
                )
            
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=page_to_update,
                request=request,
                identifier='page'
            )
        else:
            return Response(
                data=get_exception_message(400, 'page'),
                status=400
            )

    def retrieve ( self, request, pk=None ):
        return serialize_query(
            serializer=self.serializer_class,
            request=request,
            identifier='page',
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
            return Response(data=get_exception_message(404, 'page'), status=404)
        return serialize_queryset(
            serializer=self.serializer_class, 
            request=request,
            identifier='pages',
            query={
                'user': request.user,
                'date_archived__isnull': True,
                'board': current_board.id
            }
        )

    # TODO PageViewSet
    # [ ] def @action archive 
    # [ ] def @action unarchive
    # [ ] def @action page_unsorted
    # [ ] def @action page_archived
    # [ ] def @action retrieve_archived
