# coding: utf-8
from .base import *  # noqa

# Debug
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Env bar
INSTALLED_APPS += ['env_bar']
MIDDLEWARE_CLASSES = ['env_bar.middleware.EnvBarMiddleware'] + MIDDLEWARE_CLASSES

ENV_BAR_ENVIRONMENT = 'Staging'

# Debug Toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE_CLASSES = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE_CLASSES

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'samples.utils.debug_toolbar.show_toolbar'
}
