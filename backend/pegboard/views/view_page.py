from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from django.utils import timezone

from ..models import Page
from ..serializers import PageSerializer

from .utils import serialize_query, serialize_and_create, serialize_and_update, serialize_queryset

class PageViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]

    queryset = Page.objects.all()
    serializer_class = PageSerializer

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
            return Response(str(e), status=404)
        
    
    @action( detail=False, url_path='unsorted' )
    def list_unsorted(self, request):
        return serialize_queryset(
            queryset=Page.objects.list_unsorted(user=request.user),
            serializer=self.serializer_class,
        )
        
    def create(self, request):
        return serialize_and_create(
            serializer=self.serializer_class,
            request=request,
        )
    
    def update(self, request, pk=None):
        return serialize_and_update(
            serializer=self.serializer_class,
            object_to_update=Page.objects.retrieve(user=request.user, pk=pk),
            request=request,
        )

    @action( methods=['put'], detail=True, url_path='archive' )
    def archive(self, request, pk=None):
        return self.update(request, pk)

    @action( methods=['put'], detail=True, url_path='unarchive' )
    def unarchive(self, request, pk):
        return self.update(request, pk)
