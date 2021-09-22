from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone

from ..models import Page, Board
from ..serializers import PageSerializer

from .utils import serialize_query, serialize_and_create, serialize_and_update, serialize_queryset

class PageViewSet ( viewsets.ModelViewSet ):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def validate_page(self, request):
        if 'board' in request.data.keys():
            try:
                get_object_or_404(Board, pk=request.data['board'], user=request.user)
            except:
                return False
        return True

    def list(self, request):
        return serialize_queryset(
            queryset=Page.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def retrieve(self, request, pk=None):
        try:
            return serialize_query(
                query_object=Page.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class,
            )
        except Exception as e:
            return Response(e, status=404)
        
    
    @action( detail=False, url_path='unsorted' )
    def list_unsorted(self, request):
        return serialize_queryset(
            queryset=Page.objects.list_unsorted(user=request.user),
            serializer=self.serializer_class,
        )
        
    def create(self, request):
        if self.validate_page(request):
            return serialize_and_create(
                serializer=self.serializer_class,
                request=request,
                identifier='pages',
            )
        else:
            return Response('An error validating the data occurred.', status=500)
    
    def update(self, request, pk=None):
        if self.validate_page(request):
            try:
                page_to_update = get_object_or_404(Page, pk=pk, user=request.user)
                return serialize_and_update(
                    serializer=self.serializer_class,
                    object_to_update=Page.objects.retrieve(user=request.user, pk=pk),
                    request=request,
                    data=request.data,
                    identifier='page'
                )
            except Exception as e:
                return Response(e, status=500)
        else:
            return Response('An error validating the data occurred.', status=500)

    
    @action( methods=['put'], detail=True, url_path='archive' )
    def archive(self, request, pk):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Page.objects.retrieve(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': timezone.now()
                },
                identifier='page',
            )
        except Exception as e:
            return Response(e, status=404)

    @action( methods=['put'], detail=True, url_path='archive' )
    def unarchive(self, request, pk):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Page.objects.retrieve(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': None,
                },
                identifier='page',
            )
        except Exception as e:
            return Response(e, status=404)
