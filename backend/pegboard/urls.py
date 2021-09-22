from django.urls import include, path
from rest_framework import routers

from . import views

# Django Rest Framework Setup
router = routers.DefaultRouter()
# router.register(r'profiles', views.ProfileViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'pages', views.PageViewSet)
router.register(r'boards', views.BoardViewSet)
router.register(r'folders', views.FolderViewSet)
router.register(r'themes', views.ThemeViewSet)

urlpatterns = [

    # Pages
    path('', views.home_page, name='home_page'),
    path('api/', include(router.urls)),

    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
