from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import Theme
from ..serializers import ThemeSerializer

from .utils import serialize_queryset, serialize_query

class ThemeViewSet ( viewsets.ModelViewSet ):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

    # def list ( self, request ):
    #     return serialize_queryset(
    #         queryset = self.queryset.filter(user=request.user), 
    #         serializer = self.serializer_class,
    #     )

    # def retrieve ( self, request, pk=None ):
    #     return serialize_query(
    #         serializer = self.serializer_class, 
    #         request = request
    #     )
    
    # TODO ThemeViewSet
    # @ def create
    # @ def update
    # @ def partial_update
    # @ def archive @action