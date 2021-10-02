from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from django.utils import timezone

from ..models import Note
from ..serializers import NoteSerializer

from .utils import serialize_and_create, serialize_and_update, serialize_query, serialize_queryset

# TODO <NoteViewSet> `destroy`


class NoteViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request):
        try:
            return serialize_queryset(
                queryset=Note.objects.list(user=request.user),
                serializer=self.serializer_class,
            )
        except Exception as e:
            print('Error listing notes:', e)
            return Response(str(e), status=404)

    def retrieve(self, request, pk=None):
        try:
            return serialize_query(
                query_object=Note.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class,
            )
        except Exception as e:
            print('Error retrieving note:', e)
            return Response(str(e), status=404)
    
    @action(detail=False, url_path='unsorted')
    def list_unsorted(self, request):
        return serialize_queryset(
            queryset=Note.objects.list_unsorted(user=request.user),
            serializer=self.serializer_class,
        )

    def create(self, request):
        return serialize_and_create(
            serializer=self.serializer_class,
            user=request.user,
            data=request.data
        )
    
    def update(self, request, pk=None):
        return serialize_and_update(
            serializer=self.serializer_class,
            object_to_update=Note.objects.retrieve(user=request.user, pk=pk),
            user=request.user,
            data=request.data
        )
    
    @action( methods=['put'], detail=True, url_path='archive' )
    def archive ( self, request, pk ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Note.objects.retrieve(user=request.user, pk=pk),
                data={
                    'date_archived': timezone.now()
                },
            )
        except Exception as e:
            return Response(str(e), status=404)

    @action( methods=['put'], detail=True, url_path='archive' )
    def unarchive ( self, request, pk ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Note.objects.retrieve(user=request.user, pk=pk),
                data={
                    'date_archived': None,
                },
            )
        except Exception as e:
            return Response(str(e), status=404)
