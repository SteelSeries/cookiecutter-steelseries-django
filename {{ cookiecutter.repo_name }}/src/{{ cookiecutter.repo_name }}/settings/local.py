# coding: utf-8
from .base import *  # noqa

# Debug
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Allow everything, so we can set something memorable in our hosts file if we want
ALLOWED_HOSTS = ['*']

# Multiple projects running on localhost messes with sessions:
SESSION_COOKIE_NAME = "{{ cookiecutter.repo_name }}-sessionid"

# Use assets with source maps etc instead of minified assets
STATICFILES_DIRS = (
    PROJECT_DIR.ancestor(1).child('assets', '_build', 'local'),
    PROJECT_DIR.ancestor(1).child('assets', '_build', 'img'),
)

# Debug Toolbar
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INTERNAL_IPS = ('127.0.0.1',)
