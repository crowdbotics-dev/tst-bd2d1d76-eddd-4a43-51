"""
WSGI config for tst_bd2d1d76_eddd_4a43_51 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_bd2d1d76_eddd_4a43_51.settings"
)

application = get_wsgi_application()
