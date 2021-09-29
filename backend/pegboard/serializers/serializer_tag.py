
from rest_framework import serializers

from . import *
from users.serializers import UserSerializer
from ..models import Tag

class TagSerializer ( serializers.ModelSerializer ):
    model = Tag

    user = UserSerializer()
    color = ColorSerializer()

    class Meta:
        model = Tag
        fields = '__all__'
