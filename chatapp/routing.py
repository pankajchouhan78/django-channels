from django.urls import re_path
from .import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$",consumers.ChatConsumer.as_asgi()),
    # ws://127.0.0.1:9001/ws/chat/room_name/
    re_path(r'ws/test/(?P<test_name>\w+)/$', consumers.test_consumer.as_asgi()), 
    # ws://127.0.0.1:9001/test/test_name/

]