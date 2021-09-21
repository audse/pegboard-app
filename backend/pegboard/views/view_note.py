from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Note, Page
from ..serializers import NoteSerializer

from .utils import get_exception_message, serialize_and_create, serialize_and_update, serialize_queryset, serialize_query

# TODO replace `user` query with `shared_with`

class NoteViewSet ( viewsets.ModelViewSet ):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def validate_note ( self, request ):
        valid = True
        if 'page' in request.data.keys():
            try:
                current_page = get_object_or_404(Page, user=request.user, pk=request.data['page'])
            except:
                return False
        return valid


    def list ( self, request ):
        return serialize_queryset(
            serializer = self.serializer_class, 
            request = request,
            identifier = 'notes',
            query = {
                'user': request.user,
                'date_archived__isnull': True
            }
        )

    def create ( self, request ):
        if self.validate_note(request):
            return serialize_and_create(
                serializer=self.serializer_class,
                request=request,
                identifier='note'
            )
        else:
            return Response(
                data=get_exception_message(400, 'note'),
                status=400
            )
    
    def update ( self, request, pk=None ):
        if self.validate_note(request):

            note_to_update = None
            try:
                note_to_update = get_object_or_404(Note, pk=pk, user=request.user)
            except:
                return Response(
                    data=get_exception_message(404, 'note'),
                    status=404
                )
            
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=note_to_update,
                request=request,
                identifier='note'
            )
        else:
            return Response(
                data=get_exception_message(400, 'note'),
                status=400
            )


    def retrieve ( self, request, pk=None ):
        return serialize_query(
            serializer=self.serializer_class, 
            request=request,
            identifier='note',
            query={
                'pk': pk,
                'user': request.user,
                'date_archived__isnull': True
            }
        )

    @action( methods=['get'], detail=True, url_path='page' )
    def get_by_page ( self, request, pk ):
        current_page = None
        try:
            current_page = Page.objects.get(pk=pk, user=request.user, date_archived__isnull=True)
        except:
            return Response(data=get_exception_message(404, 'page'), status=404)

        return serialize_queryset(
            serializer=self.serializer_class,
            request=request,
            identifier='notes',
            query={
                'user': request.user,
                'page': current_page,
                'date_archived__isnull': True,
            }
        )
    
    # TODO NoteViewSet
    # [ ] def @action archive
    # [ ] def @action unarchive
    # [ ] def @action list_unsorted
    # [ ] def @action list_archived
    # [ ] def @action retrieve_archived