# coding: utf-8
from __future__ import absolute_import
try:
    from .celery import app  # noqa
except ImportError:
    pass
