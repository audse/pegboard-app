# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class FolderConsumer(WebsocketConsumer):
    def connect(self):
        self.folder_id = self.scope['url_route']['kwargs']['folder_id']
        self.folder_url = self.scope['url_route']['kwargs']['folder_url']

        self.folder_group_name = 'folder-'+str(self.folder_id)+'_'+self.folder_url

        async_to_sync(self.channel_layer.group_add)(
            self.folder_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.folder_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        name = text_data_json['name']

        async_to_sync(self.channel_layer.group_send)(
            self.folder_group_name, {
                'type': 'create_folder',
                'name': name
            }
        )

    def create_folder(self, event):
        name = event['name']

        self.send(text_data=json.dumps({
            'name': name
        }))