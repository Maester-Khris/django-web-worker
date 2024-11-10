"""
ASGI config for djangoworker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import threading
from scrapper.worker import launch_scrapper

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoworker.settings')

application = get_asgi_application()

threading.Thread(target=launch_scrapper).start()
