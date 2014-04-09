# coding: utf-8
import logging
from datetime import datetime

try:
    from celery.app.log import TaskFormatter as _TaskFormatter
except ImportError:
    _TaskFormatter = None


class MicrosecondFormatter(logging.Formatter):

    def formatTime(self, record, **kwargs):
        ct = datetime.fromtimestamp(record.created)
        return ct.strftime('%Y-%m-%dT%H:%M:%S.%f')


if _TaskFormatter:
    class TaskFormatter(MicrosecondFormatter, _TaskFormatter):
        pass
