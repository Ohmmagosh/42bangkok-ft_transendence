# chat/consumers.py
import json
import asyncio

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


class PingPongConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"game_{self.room_name}"
        self.ball_position = {'x': 0, 'y': 200}

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()
        self.start_game_loop()
        
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                'type': 'game.action',
                'action': action,
                'position': self.ball_position,
                }
        )

    async def update_ball_position(self):
        self.ball_position['x'] += 5
        
        # async_to_sync(self.channel_layer.group_send)(
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'game.action',
                'action': 'update_ball_position',
                'position': self.ball_position,
            }
        )
        
    def start_game_loop(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.update_loop())
        
    async def update_loop(self):
        while True:
            await self.update_ball_position()
            await asyncio.sleep(0.1)
            
    # Receive message from room group
    async def game_action(self, event):
        action = event["action"]
        position = event["position"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"action": action, 'position': position}))

