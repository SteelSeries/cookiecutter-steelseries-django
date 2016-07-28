# coding: utf-8
from .base import *  # noqa

# Debug
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Multiple projects running on localhost messes with sessions:
SESSION_COOKIE_NAME = "{{ cookiecutter.repo_name }}-sessionid"

# Env bar
INSTALLED_APPS += ['env_bar']
MIDDLEWARE_CLASSES = ['env_bar.middleware.EnvBarMiddleware'] + MIDDLEWARE_CLASSES

ENV_BAR_ENVIRONMENT = 'Development'

# Debug Toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE_CLASSES = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE_CLASSES

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': '{{ cookiecutter.repo_name }}.utils.debug_toolbar.show_toolbar'
}
