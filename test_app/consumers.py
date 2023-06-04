import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class TestConsumers(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected'}))

    def receive(self, text_data):
        print(text_data)

    def disconnect(self, *args, **kwargs):
        print("Disconnected to the server")