from __future__ import unicode_literals
from rest_framework import viewsets

from django.contrib.auth.models import User
from ..serializers import ProfileSerializer

from .utils import serialize_queryset, serialize_query

class ProfileViewSet ( viewsets.ModelViewSet ):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset=self.queryset, 
            serializer=self.serializer_class, 
            request=request,
            identifier='profiles'
        ))

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = User, 
            pk = pk, 
            serializer = self.serializer_class, 
            request = request, 
            identifier = 'profile', 
            requires_auth=False
        ))
    
    # TODO ProfileViewSet
    # @ def create
    # @ def update
    # @ def partial_update

