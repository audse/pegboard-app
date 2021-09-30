import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.auth import login
from rest_framework.authentication import TokenAuthentication

from ..models import Board
from ..serializers import BoardSerializer, PageSerializer, NoteSerializer, TagSerializer, ColorSerializer
from ..views import BoardViewSet

class BoardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await database_sync_to_async(self.scope['session'].save)()

        self.user = self.scope['user']

        self.board_id = self.scope['url_route']['kwargs']['board_id']
        self.board_url = self.scope['url_route']['kwargs']['board_url']

        self.board_group_name = 'board-'+str(self.board_id)+'-'+self.board_url

        self.board_with_children = await self.retrieve_with_children()

        await self.channel_layer.group_add(
            self.board_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.board_group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        text_data_json = json.loads(text_data)
        action = text_data_json['action']

        if action == 'retrieveWithChildren':
            await self.channel_layer.group_send(
                self.board_group_name,
                {
                    'type': 'send_retrieve_with_children',
                }
            )

    async def send_retrieve_with_children(self, event):
        await self.send(text_data=json.dumps({
            'action': 'retrieveWithChildren',
            'response': self.board_with_children
        }))

    async def update(self, event):
        self.board_with_children = await self.retrieve_with_children()
        await self.channel_layer.group_send(
            self.board_group_name,
            {
                'type': 'send_retrieve_with_children',
            }
        )

    @database_sync_to_async
    def retrieve_with_children(self):
        response = None
        try:
            original_response = Board.objects.retrieve_with_children(user=self.user, pk=self.board_id)
            response = {
                'board': BoardSerializer(original_response['board']).data,
                'tags': TagSerializer(original_response['tags'], many=True).data,
                'pages': [],
            }

            for page in original_response['pages']:

                response['pages'].append({
                    'page': PageSerializer(page['page']).data,
                    'notes': NoteSerializer(page['notes'], many=True).data
                })

        except Exception as e:
            response = str(e)

        return response
