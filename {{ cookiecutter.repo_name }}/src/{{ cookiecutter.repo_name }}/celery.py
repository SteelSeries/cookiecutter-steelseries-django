# coding: utf-8
from __future__ import absolute_import

try:
    from celery import Celery
except ImportError:
    Celery = None


if Celery:
    from django.conf import settings

    app = Celery('{{ cookiecutter.repo_name }}')
    app.config_from_object('django.conf:settings')
    app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
else:
    app = None
