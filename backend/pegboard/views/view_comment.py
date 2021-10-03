from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from ..models import Comment
from ..serializers import CommentSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class CommentViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
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
        return serialize_and_create(
            serializer=self.serializer_class,
            request=request,
        )
    
    def update(self, request, pk=None):
        return serialize_and_update(
            serializer=self.serializer_class,
            object_to_update=Comment.objects.retrieve(user=request.user, pk=pk),
            request=request,
        )

    @action( methods=['put'], detail=True, url_path='archive' )
    def archive(self, request, pk=None):
        return self.update(request, pk)

    @action( methods=['put'], detail=True, url_path='unarchive' )
    def unarchive(self, request, pk):
        return self.update(request, pk)
