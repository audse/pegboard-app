from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        print('\n\nSCOPE', scope, '\n\n')
        try:
            token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
        except ValueError:
            token_key = None
        scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)
        return await super().__call__(scope, receive, send)

# class GetUserMiddleware(BaseMiddleware):
#     def __init__(self, inner):
#         super().__init__(inner)
    
#     async def __call__(self, scope, receive, send):
#         print('\n\nSCOPE', scope['headers'], '\n\n')
#         # print('\n\nUSER', scope, '\n\n')

#         return await super().__call__(scope, receive, send)



# SCOPE {'type': 'websocket', 'path': '/ws/api/folders', 'raw_path': b'/ws/api/folders', 
# 'headers': [(b'upgrade', b'websocket'), (b'connection', b'Upgrade'), (b'host', b'localhost:8000'), 
# (b'origin', b'http://localhost:3000'), (b'pragma', b'no-cache'), (b'cache-control', b'no-cache'), 
# (b'sec-websocket-key', b'EyXJGm6rBN+6DUQggFA63Q=='), (b'sec-websocket-version', b'13'), 
# (b'sec-websocket-extensions', b'x-webkit-deflate-frame'), 
# (b'user-agent', b'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'), 
# (b'cookie', b'csrftoken=J5PKIIuFTiOEHHVHWQ1v66b1T5x8sfdyyOPRYBRg5h3jkjoRsGU6SICWksf1Kjn8; sessionid=dlw360tna2xbpnhbs2zl6ecmcy057bkh; tabstyle=html-tab; auth._token.local=Token%203ff6fec19f69fccd1a3c70e8648441a2bd4ba405; auth._token_expiration.local=1632042235940; auth.strategy=local')], 
# 'query_string': b'', 'client': ['127.0.0.1', 52993], 'server': ['127.0.0.1', 8000], 'subprotocols': [], 'asgi': {'version': '3.0'}} 