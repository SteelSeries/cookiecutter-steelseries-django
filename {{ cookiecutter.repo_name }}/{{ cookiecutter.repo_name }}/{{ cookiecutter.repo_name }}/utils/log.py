# coding: utf-8
import logging
from datetime import datetime

try:
    from celery._state import get_current_task
except ImportError:
    get_current_task = None


class MicrosecondFormatter(logging.Formatter):

    def formatTime(self, record, **kwargs):
        ct = datetime.fromtimestamp(record.created)
        return ct.strftime('%Y-%m-%dT%H:%M:%S.%f')


if get_current_task:
    class TaskFormatter(MicrosecondFormatter):

        def format(self, record):
            task = get_current_task()
            if task and task.request:
                record.__dict__.update(task_id=task.request.id, task_name=task.name)
            else:
                record.__dict__.setdefault('task_name', '???')
                record.__dict__.setdefault('task_id', '???')
            return logging.Formatter.format(self, record)
