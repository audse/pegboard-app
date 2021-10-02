from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from ..models import Color
from ..serializers import ColorSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class ColorViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]

    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    
    def list(self, request):
        return serialize_queryset(
            queryset=Color.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query(
                query_object=Color.objects.retrieve(user=request.user, pk=pk),
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
            object_to_update=Color.objects.retrieve(user=request.user, pk=pk),
            request=request,
        )
