from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone

from ..models import Note, Page
from ..serializers import NoteSerializer

from .utils import serialize_and_create, serialize_and_update, serialize_query, serialize_queryset

# TODO <NoteViewSet> `destroy`


class NoteViewSet ( viewsets.ModelViewSet ):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def validate_note(self, request):
        if 'page' in request.data.keys():
            try:
                get_object_or_404(Page, pk=request.data['page'], user=request.user)
            except:
                return False
        return True

    def list(self, request):
        return serialize_queryset(
            queryset=Note.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def retrieve(self, request, pk=None):
        try:
            return serialize_query(
                query_object=Note.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class,
            )
        except Exception as e:
            return Response(e, status=404)
    
    @action(detail=False, url_path='unsorted')
    def list_unsorted(self, request):
        return serialize_queryset(
            queryset=Note.objects.list_unsorted(user=request.user),
            serializer=self.serializer_class,
        )

    def create(self, request):
        if self.validate_note(request):
            return serialize_and_create(
                serializer=self.serializer_class,
                request=request,
                identifier='notes',
            )
        else:
            return Response('An error validating the data occurred.', status=500)
    
    def update(self, request, pk=None):
        if self.validate_note(request):
            try:
                return serialize_and_update(
                    serializer=self.serializer_class,
                    object_to_update=Note.objects.retrieve(user=request.user, pk=pk),
                    request=request,
                    data=request.data,
                    identifier='note'
                )
            except Exception as e:
                return Response(e, status=404)
        else:
            return Response('An error validating the data occurred.', status=500)

        
    
    @action( methods=['put'], detail=True, url_path='archive' )
    def archive ( self, request, pk ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Note.objects.retrieve(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': timezone.now()
                },
                identifier='note',
            )
        except Exception as e:
            return Response(e, status=404)

    @action( methods=['put'], detail=True, url_path='archive' )
    def unarchive ( self, request, pk ):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Note.objects.retrieve(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': None,
                },
                identifier='note',
            )
        except Exception as e:
            return Response(e, status=404)
