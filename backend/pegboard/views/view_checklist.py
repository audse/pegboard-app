from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from djangochannelsrestframework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.utils import timezone

from ..models import Board, Checklist, Page, Note
from ..serializers import ChecklistSerializer

from .utils import serialize_queryset, serialize_query, serialize_and_create, serialize_and_update

class ChecklistViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer

    def validate_checklist(self, request):
        if 'board' in request.data.keys():
            try:
                get_object_or_404(Board, pk=request.data['board'])
            except:
                return False
        if 'page' in request.data.keys():
            try:
                get_object_or_404(Page, pk=request.data['page'])
            except:
                return False
        if 'note' in request.data.keys():
            try:
                get_object_or_404(Note, pk=request.data['note'])
            except:
                return False
        return True
    
    def list(self, request):
        return serialize_queryset(
            queryset=Checklist.objects.list(user=request.user),
            serializer=self.serializer_class,
        )

    def retrieve ( self, request, pk=None ):
        try:
            return serialize_query(
                query_object=Checklist.objects.retrieve(user=request.user, pk=pk),
                serializer=self.serializer_class, 
            )
        except Exception as e:
            return Response(e, status=404)
    
    def create(self, request):
        if self.validate_checklist(request):
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
        if self.validate_checklist(request):
            try:
                return serialize_and_update(
                    serializer=self.serializer_class,
                    object_to_update=Checklist.objects.retrieve(user=request.user, pk=pk),
                    data=request.data,
                )
            except Exception as e:
                return Response(str(e), status=404)
        else:
            return Response('An error validating the data occurred.', status=500)