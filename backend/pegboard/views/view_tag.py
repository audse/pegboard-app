from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from ..models import Tag
from ..serializers import TagSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class TagViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    def list(self, request):
        return serialize_queryset(
            queryset=Tag.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query(
                query_object=Tag.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class, 
            )
        except Exception as e:
            return Response(e, status=404)
    
    def create(self, request):
        return serialize_and_create(
            serializer=self.serializer_class,
            request=request,
        )
    
    def update(self, request, pk=None):
        return serialize_and_update(
            serializer=self.serializer_class,
            object_to_update=Tag.objects.retrieve(user=request.user, pk=pk),
            request=request,
        )
