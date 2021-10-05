import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.auth import login
from rest_framework.authentication import TokenAuthentication

from ..models import Board
from ..serializers import BoardSerializer, PageSerializer, TagSerializer, ChecklistSerializer
from ..views import BoardViewSet

class BoardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await database_sync_to_async(self.scope['session'].save)()

        self.user = self.scope['user']

        self.board_id = self.scope['url_route']['kwargs']['board_id']
        self.board_url = self.scope['url_route']['kwargs']['board_url']

        self.board_group_name = 'board-'+str(self.board_id)+'-'+self.board_url
        print('\nConnected to', self.board_group_name, '!\n')

        self.board = await self.retrieve()

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

        if action == 'retrieve':
            await self.channel_layer.group_send(
                self.board_group_name,
                {
                    'type': 'send_retrieve',
                }
            )

    async def send_retrieve(self, event):
        await self.send(text_data=json.dumps({
            'action': 'retrieve',
            'response': self.board
        }))

    async def update(self, event):
        print('Updating websocket...')
        self.board = await self.retrieve()
        await self.channel_layer.group_send(
            self.board_group_name,
            {
                'type': 'send_retrieve',
            }
        )

    @database_sync_to_async
    def retrieve(self):
        try:
            return BoardSerializer(Board.objects.retrieve(user=self.user, pk=self.board_id)).data
        except Exception as e:
            return str(e)