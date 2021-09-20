from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
# from rest_framework.authtoken import views
from .views import GoogleLogin
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/', views.obtain_auth_token),
    path('google/', GoogleLogin.as_view(), name='google_login'),
]