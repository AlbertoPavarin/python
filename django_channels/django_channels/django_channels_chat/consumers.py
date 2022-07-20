import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumers(WebsocketConsumer):
    def connect(self):
        self().accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json['message']

        print(message)