"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter

import channels_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Add more ASGI apps here if needed
    'websocket': URLRouter(channels_app.routing.ws_urlpatterns,
                           ),
})