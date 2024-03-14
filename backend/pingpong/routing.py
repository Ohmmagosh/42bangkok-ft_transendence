from django.urls import re_path

from .import consumers


websocket_urlpatterns = [
    re_path(r"ws/pingpong/(?P<room_name>\w+)/$", consumers.PingPongConsumer.as_asgi()),
    ]