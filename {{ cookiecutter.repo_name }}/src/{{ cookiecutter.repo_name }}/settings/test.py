# coding: utf-8
from .base import *  # noqa

# We add some packages here to include static files in build
INSTALLED_APPS += ['debug_toolbar', 'env_bar']

# Add jenkins for testing and reporting
INSTALLED_APPS += ['django_jenkins']
