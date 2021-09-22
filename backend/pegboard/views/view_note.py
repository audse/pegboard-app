from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.utils import timezone

from ..models import Note, Page
from ..serializers import NoteSerializer

from .utils import get_exception_message, serialize_and_create, serialize_and_update, serialize_queryset, serialize_query, serialize_query_without_args, serialize_queryset_without_args

# TODO <NoteViewSet> `destroy`


class NoteViewSet ( viewsets.ModelViewSet ):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def validate_note ( self, request ):
        if 'page' in request.data.keys():
            try:
                get_object_or_404(Page, pk=request.data['page'], user=request.user)
            except:
                return False
        return True

    def list ( self, request ):
        return serialize_queryset_without_args(
            queryset=Note.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def create ( self, request ):
        if self.validate_note(request):
            return serialize_and_create(
                serializer=self.serializer_class,
                request=request,
                identifier='notes',
            )
        else:
            return Response(
                data=get_exception_message(404, 'note'),
                status=404
            )
    
    def update ( self, request, pk=None ):
        if self.validate_note(request):
            try:
                return serialize_and_update(
                    serializer=self.serializer_class,
                    object_to_update=Note.objects.retrieve(user=request.user, pk=pk),
                    request=request,
                    data=request.data,
                    identifier='note'
                )
            except:
                return Response(
                    data=get_exception_message(404, 'note'),
                    status=404
                )
        else:
            return Response(
                data=get_exception_message(400, 'note'),
                status=400
            )

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query_without_args(
                query_object=Note.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class,
            )
        except Exception as e:
            return Response(e, status=404)

    @action( methods=['get'], detail=True, url_path='page' )
    def list_by_page ( self, request, pk ):
        try:
            current_page = Page.objects.retrieve(user=request.user, pk=pk)
            return serialize_queryset_without_args(
                queryset=Note.objects.list_by_page(user=request.user, page=current_page),
                serializer=self.serializer_class, 
        )
        except Exception as e:
            return Response(e, status=404)
        
    
    @action( methods=['get'], detail=True, url_path='unsorted')
    def list_unsorted ( self, request ):
        return serialize_queryset_without_args(
            queryset=Note.objects.list_unsorted(user=request.user),
            serializer=self.serializer_class,
        )
    
    @action( methods=['get'], detail=True, url_path='archived' )
    def list_archived ( self, request ):
        return serialize_queryset_without_args(
            queryset=Note.objects.list_archived(user=request.user),
            serializer=self.serializer_class,
        )
    
    @action( methods=['get'], detail=True, url_path='archived' )
    def retrieve_archived ( self, request, pk ):
        try:
            return serialize_query_without_args(
                query_object=Note.objects.retrieve_archived(user=request.user, pk=pk),
                serializer=self.serializer_class,
            )
        except Exception as e:
            return Response(e, status=404)
    
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
                object_to_update=Note.objects.retrieve_archived(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': None,
                },
                identifier='note',
            )
        except Exception as e:
            return Response(e, status=404)
