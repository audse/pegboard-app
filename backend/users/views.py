# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView, SocialLoginSerializer
# # from allauth.socialaccount.providers.google.views import GoogleOAuth2RestAdapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from django.views.decorators.csrf import csrf_exempt
# from google.oauth2 import id_token, credentials
# from google.auth.transport import requests

# from .models import SocialProfile

# from rest_framework.response import Response
    
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from .serializers import UserSerializer

# class UserViewSet(viewsets.ModelViewSets):
#     authentication_classes = [TokenAuthentication]
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


# class GoogleLogin(SocialLoginView):
    # authentication_classes = [] # disable authentication
    # adapter_class = GoogleOAuth2Adapter
    # callback_url = 'http://localhost:3000'
    # client_class = OAuth2Client

# def GoogleSignUp (request):
#     # Get JSON Web Token
#     token = None
#     try:
#         token = request.data['token']
#     except Exception as err:
#         return Response(err)

#     # Access User Data
#     try:
#         decrypted_token = id_token.verify_oauth2_token(token, requests.Request(), '652460956969-394v9crnmp6hf9pugt6vua5vsrin5odr.apps.googleusercontent.com')
#         return Response()

#     except Exception as err:
#         return Response(err)


# class GoogleLogin(SocialLoginView):
#     authentication_classes = []
#     adapter_class = GoogleOAuth2Adapter
#     client_class = OAuth2Client
#     serializer_class = SocialLoginSerializer
#     callback_url = 'http://localhost:3000/login'

#     def get_serializer(self, *args, **kwargs):
#         serializer_class = self.get_serializer_class()
#         kwargs['context'] = self.get_serializer_context()
#         return serializer_class(*args, **kwargs)
    
#     @csrf_exempt
#     def post(self, request, *args, **kwargs):
#         token = None
#         try:
#             token = request.data['token']
#         except Exception as err:
#             print('FAILED TO GET TOKEN FROM REQUEST', err)
#             return Response()

#         try:
#             # Specify the CLIENT_ID of the app that accesses the backend:
#             decrypted_token = id_token.verify_oauth2_token(token, requests.Request(), '652460956969-394v9crnmp6hf9pugt6vua5vsrin5odr.apps.googleusercontent.com')
#             decrypted_user_id = decrypted_token['sub']
#             print(decrypted_token)
#             super().post(request=request, data={'access_token':token})
#         except Exception as err:
#             print('FAILED TO VERIFY TOKEN', err)
#             return Response()