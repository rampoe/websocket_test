import os

from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from test_app.consumers import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

application = get_asgi_application()

ws_patterns = [
    path('ws/testapp/', TestConsumers.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patterns)
})
