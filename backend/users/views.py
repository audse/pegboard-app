from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView, SocialLoginSerializer
# from allauth.socialaccount.providers.google.views import GoogleOAuth2RestAdapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.views.decorators.csrf import csrf_exempt

# class GoogleLogin(SocialLoginView):
    # authentication_classes = [] # disable authentication
    # adapter_class = GoogleOAuth2Adapter
    # callback_url = 'http://localhost:3000'
    # client_class = OAuth2Client

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
#         print(request.data)
#         return super().post(request)

