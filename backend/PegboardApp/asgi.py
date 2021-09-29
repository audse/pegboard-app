from django.urls import path
from djangochannelsrestframework.consumers import view_as_consumer

from users.middleware import TokenAuthMiddleware
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import pegboard

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PegboardApp.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    'websocket': TokenAuthMiddleware(
        URLRouter([
            path('ws/api/folders', view_as_consumer(
                pegboard.views.FolderViewSet.as_view({
                    'get': 'list'
                })))
        ])
    ),
})