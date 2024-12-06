"""
WSGI config for studentapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
project_home = '/home/yourusername/yourprojectdirectory'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'studentapp.settings'
"""
# Activate your virtual environment
activate_this = '/home/yourusername/yourprojectdirectory/myenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
"""
# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()