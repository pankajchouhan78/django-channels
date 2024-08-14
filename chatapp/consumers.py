import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        test_data_json = json.loads(text_data)
        message = test_data_json['message']
       
        user = self.scope["user"]
        username = user.username if user.is_authenticated else 'Anonymous'

        # Send message to room group with sender information
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message,
                "sender": username
            }
        )

    
     # Receive message from room group
    def chat_message(self, event):

        message = event["message"]
        sender = event["sender"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "message": message,
            "sender": sender
        }))

     