from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.utils import timezone

from ..models import Board, Color
from ..serializers import ColorSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class ColorViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

    def validate_color(self, request):
        if 'board' in request.data.keys():
            try:
                get_object_or_404(Board, pk=request.data['board'])
            except:
                return False
        return True
    
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
        if self.validate_color(request):
            return serialize_and_create(
                serializer=self.serializer_class,
                data={
                    'user': request.user.pk,
                    **request.data
                }
            )
        else:
            return Response('An error validating the data occurred.', status=500)
    
    def update(self, request, pk=None):
        if self.validate_color(request):
            try:
                return serialize_and_update(
                    serializer=self.serializer_class,
                    object_to_update=Color.objects.retrieve(user=request.user, pk=pk),
                    data=request.data,
                )
            except Exception as e:
                return Response(str(e), status=404)
        else:
            return Response('An error validating the data occurred.', status=500)