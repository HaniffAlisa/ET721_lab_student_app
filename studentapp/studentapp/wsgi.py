"""
WSGI config for studentapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentapp.settings'

# Activate your virtual environment
activate_this = '/home/yourusername/yourprojectdirectory/myenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studentapp.settings")

application = get_wsgi_application()
