# from channels.generic.websocket import AsyncWebsocketConsumer 
# import json, time
# from .forms import MessageForm
# from .models import ChatMessage
# from channels.db import database_sync_to_async

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_id = str(self.scope['url_route']['kwargs']['group_id'])
        
#         await self.channel_layer.group_add(
#             self.group_id,
#             self.channel_name
#         )
        
#         await self.accept()
        
#     async def receive(self, text_data):
#         saved_message = await self.save_message(text_data)
        
#         await self.channel_layer.group_send(
#             self.group_id,
#             {
#                 'type': 'send_message_to_chat',
#                 'text_data': text_data,
#                 'username': self.scope['user'].email,
#                 'datetime': saved_message.date_time.isoformat(),
#             }
#         )
        
        
#     async def send_message_to_chat(self, event):
#         dict_data = json.loads(event['text_data'])
#         form = MessageForm(dict_data)
        
#         if form.is_valid():
#             text_to_send = f"{event['username']}: {dict_data['message']}"
#             text_data = json.dumps({
#                 'message': text_to_send,
#                 'datetime': event['datetime'],
#             }, ensure_ascii = False)
            
#             await self.send(text_data)
#         else:
#             print("Form is not valid:", form.errors)
            
#     @database_sync_to_async
#     def save_message(self, text_data):
#         user = self.scope['user']
#         message_data = json.loads(message_data)
        
#         message = ChatMessage.objects.create(
#             content = message_data['message'],
#             author = user,
#             chat_group_id = self.group_id,
#             date_time = time.time()
#         )
#         return message
                