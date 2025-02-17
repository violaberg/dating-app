"""
WSGI config for dating_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

if 'daphne' in sys.argv[0].lower():
    print("DEBUG Daphne is running.")
else:
    print("DEBUG very much Daphne is NOT running, possibly using gunicorn or another server.")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dating_app.settings')

application = get_wsgi_application()
