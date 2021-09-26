from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.utils import timezone

from ..models import Board, Folder
from ..serializers import BoardSerializer, PageSerializer, NoteSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class BoardViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def validate_board(self, request):
        if 'folder' in request.data.keys():
            try:
                get_object_or_404(Folder, pk=request.data['folder'], user=request.user)
            except:
                return False
        return True
    
    def list(self, request):
        return serialize_queryset(
            queryset=Board.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query(
                query_object=Board.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class, 
            )
        except Exception as e:
            return Response(e, status=404)
    
    @action(detail=True, url_path='board')
    def retrieve_with_children(self, request, pk=None):
        try:
            response = Board.objects.retrieve_with_children(user=request.user, pk=pk)

            serialized_response = {
                'board': BoardSerializer(response['board']).data,
                'pages': [], # [ {page: xyz, notes: [a, b, c,]}, {} ]
            }

            for page in response['pages']:
                serialized_page = PageSerializer(page['page']).data

                serialized_notes = []
                for note in page['notes']:
                    serialized_notes.append(NoteSerializer(note).data)

                serialized_response['pages'].append({
                    'page': serialized_page,
                    'notes': serialized_notes
                })
            
            return Response(serialized_response)

        except Exception as e:
            print('\n\n', e, '\n\n')
            return Response(str(e), status=500)
    
    @action( methods=['get'], detail=False, url_path='unsorted')
    def list_unsorted(self, request):
        return serialize_queryset(
            queryset=Board.objects.list_unsorted(user=request.user),
            serializer=self.serializer_class,
        )

    @action( methods=['get'], detail=False, url_path='shared' )
    def list_shared_with(self, request):
        return serialize_queryset(
            queryset=Board.objects.list_shared_with(user=request.user),
            serializer=self.serializer_class,
        )
    

    @action( methods=['get'], detail=False, url_path='archived' )
    def list_archived(self, request):
        return serialize_queryset(
            queryset=Board.objects.list_archived(user=request.user),
            serializer=self.serializer_class,
        )
    
    def create(self, request):
        if self.validate_board(request):
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
        if self.validate_board(request):
            try:
                return serialize_and_update(
                    serializer=self.serializer_class,
                    object_to_update=Board.objects.retrieve(user=request.user, pk=pk),
                    data=request.data,
                )
            except Exception as e:
                return Response(str(e), status=404)
        else:
            return Response('An error validating the data occurred.', status=500)

    @action( methods=['put'], detail=True, url_path='archive' )
    def archive(self, request, pk):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Board.objects.retrieve(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': timezone.now()
                },
                identifier='board',
            )
        except Exception as e:
            return Response(e, status=404)

    @action( methods=['put'], detail=True, url_path='archive' )
    def unarchive(self, request, pk):
        try:
            return serialize_and_update(
                serializer=self.serializer_class,
                object_to_update=Board.objects.retrieve(user=request.user, pk=pk),
                request=request,
                data={
                    'date_archived': None,
                },
                identifier='board',
            )
        except Exception as e:
            return Response(e, status=404)