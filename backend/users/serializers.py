from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

class UserSerializer(UserDetailsSerializer):

    theme = serializers.CharField(source='profile.theme')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('theme',)
        # fields = ['pk', 'username', 'email']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        theme = profile_data.get('theme')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.profile
        if profile_data and theme:
            profile.theme = theme
            profile.save()
        return instance