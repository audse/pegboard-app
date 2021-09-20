from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView, SocialLoginSerializer
# from allauth.socialaccount.providers.google.views import GoogleOAuth2RestAdapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests

from rest_framework.response import Response

# class GoogleLogin(SocialLoginView):
    # authentication_classes = [] # disable authentication
    # adapter_class = GoogleOAuth2Adapter
    # callback_url = 'http://localhost:3000'
    # client_class = OAuth2Client

class GoogleLogin(SocialLoginView):
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer
    callback_url = 'http://localhost:3000/login'

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        token = None
        try:
            token = request.data['token']
        except Exception as err:
            print('FAILED TO GET TOKEN FROM REQUEST', err)
            return Response()

        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            decrypted_token = id_token.verify_oauth2_token(token, requests.Request(), '652460956969-394v9crnmp6hf9pugt6vua5vsrin5odr.apps.googleusercontent.com')
            decrypted_user_id = decrypted_token['sub']
            print(decrypted_token)
            super().post(request=request, data={'access_token':token})
        except Exception as err:
            print('FAILED TO VERIFY TOKEN', err)
            return Response()