"""
ASGI config for amgchat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from decouple import config
from django.core.asgi import get_asgi_application
from django.urls import path, re_path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.settings')

django_asgi_app = get_asgi_application()

from chat import consumers

application = ProtocolTypeRouter()
