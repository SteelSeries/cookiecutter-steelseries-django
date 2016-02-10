# coding: utf-8
from .base import *  # noqa

# Debug
DEBUG = True

# Allow everything, so we can set something memorable in our hosts file if we want
ALLOWED_HOSTS = ['*']

# Multiple projects running on localhost messes with sessions:
SESSION_COOKIE_NAME = "{{ cookiecutter.repo_name }}-sessionid"

# Don't use template caching
# TEMPLATES[0]['OPTIONS']['loaders'] = [
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader'
# ]
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Debug Toolbar
# INSTALLED_APPS += ('debug_toolbar',)
# MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INTERNAL_IPS = ('10.10.10.1', '127.0.0.1',)
