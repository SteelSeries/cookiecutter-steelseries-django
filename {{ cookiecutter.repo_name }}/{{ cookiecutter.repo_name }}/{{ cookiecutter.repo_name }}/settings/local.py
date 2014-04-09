# coding: utf-8
from .base import *  # noqa

# Debug
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Debug Toolbar
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INTERNAL_IPS = ('127.0.0.1',)
