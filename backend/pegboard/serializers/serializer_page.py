from rest_framework import serializers

from . import *
from users.serializers import UserSerializer
from ..models import Page

class PageSerializer ( serializers.ModelSerializer ):
    
    model = Page

    notes = NoteSerializer(many=True)

    class Meta:
        model = Page
        fields = '__all__'
        depth = 2