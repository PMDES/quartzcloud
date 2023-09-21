import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from django_project.consumers import MyConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": get_asgi_application(),
    }
)

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(
            [
                path("ws/", MyConsumer.as_asgi()),
            ]
        ),
    }
)
