from django.urls import include, path, re_path
from rest_framework import routers

from djangochannelsrestframework.consumers import view_as_consumer

from . import views

# Django Rest Framework Setup
router = routers.DefaultRouter()
# router.register(r'profiles', views.ProfileViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'pages', views.PageViewSet)
router.register(r'boards', views.BoardViewSet)
router.register(r'folders', views.FolderViewSet)
router.register(r'themes', views.ThemeViewSet)
router.register(r'colors', views.ColorViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'checklists', views.ChecklistViewSet)

urlpatterns = [

    # Pages
    path('', views.home_page, name='home_page'),
    path('api/', include(router.urls)),

    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
