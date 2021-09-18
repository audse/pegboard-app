from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Card, List, Board, Theme

# class ProfileSerializer ( serializers.ModelSerializer ):
#     model = User
#     class Meta:
#         model = User
#         fields = '__all__'

class CardSerializer ( serializers.ModelSerializer ):
    model = Card
    class Meta:
        model = Card
        fields = '__all__'
        # TODO add ordering here

class ListSerializer ( serializers.ModelSerializer ):
    model = List
    class Meta:
        model = List
        fields = '__all__'
    
class BoardSerializer ( serializers.ModelSerializer ):
    model = Board
    class Meta:
        model = Board
        fields = '__all__'

class ThemeSerializer ( serializers.ModelSerializer ):
    model = Theme
    class Meta:
        model = Theme
        fields = '__all__'

        from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

class UserSerializer(UserDetailsSerializer):

    theme = serializers.CharField(source='profile.theme')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('theme',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        theme = profile_data.get('theme')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.profle
        if profile_data and company_name:
            profile.theme = theme
            profile.save()
        return instance