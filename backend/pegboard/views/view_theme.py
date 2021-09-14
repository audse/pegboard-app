from __future__ import unicode_literals
from rest_framework import viewsets

from ..models import Theme
from ..serializers import ThemeSerializer

from .utils import handle_response, serialize_queryset, serialize_query

class ThemeViewSet ( viewsets.ModelViewSet ):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    def list ( self, request ):
        return handle_response( serialize_queryset(
            queryset = self.queryset.filter(user=request.user), 
            serializer = self.serializer_class, 
            request = request,
            identifier = 'themes'
        ))

    def retrieve ( self, request, pk=None ):
        return handle_response( serialize_query(
            model = Theme, 
            pk = pk, 
            serializer = self.serializer_class, 
            request = request
        ))
    
    # TODO ThemeViewSet
    # @ def create
    # @ def update
    # @ def partial_update
    # @ def archive @action