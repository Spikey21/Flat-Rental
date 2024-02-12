"""
ASGI config for rent_flat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from .routing import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rent_flat.settings')

django_asgi_app = get_asgi_application()

application = application
