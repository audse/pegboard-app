from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.utils import timezone

from ..models import Board, Comment, Page, Note
from ..serializers import CommentSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class CommentViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def validate_comment(self, request):

        validated_foreign_keys = {
            'board': None,
            'page': None,
            'note': None,
        }

        if 'board' in request.data.keys() and request.data['board'] is not None:
            get_object_or_404(Board, pk=request.data['board'])
            validated_foreign_keys['board'] = request.data['board']
            
        if 'page' in request.data.keys() and request.data['page'] is not None:
            get_object_or_404(Page, pk=request.data['page'])
            validated_foreign_keys['page'] = request.data['page']
                
        if 'note' in request.data.keys() and request.data['note'] is not None:
            get_object_or_404(Note, pk=request.data['note'])
            validated_foreign_keys['note'] = request.data['note']

        return validated_foreign_keys
    
    def list(self, request):
        return serialize_queryset(
            queryset=Comment.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query(
                query_object=Comment.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class, 
            )
        except Exception as e:
            return Response(e, status=404)
    
    def create(self, request):
        try:
            validated_foreign_keys = self.validate_comment(request)
            return serialize_and_create(
                serializer=self.serializer_class,
                data={
                    'user': request.user.pk,
                    **request.data,
                    **validated_foreign_keys
                }
            )
        except Exception as e:
            return Response(str(e), status=500)
    
    def update(self, request, pk=None):
        try:
            validated_foreign_keys = self.validate_comment(request)
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Comment.objects.retrieve(user=request.user, pk=pk),
                data={
                    **request.data,
                    **validated_foreign_keys,
                }
            )
        except Exception as e:
            return Response(str(e), status=404)
