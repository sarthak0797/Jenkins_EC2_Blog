"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
# sys.path.append('/home/humbel-fool/V_enviroment/AllinCall/website')

# add the virtualenv site-packages path to the sys.path
# sys.path.append('/home/humbel-fool/V_enviroment/Lib/site-packages')

# poiting to the project settings

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

application = get_wsgi_application()
