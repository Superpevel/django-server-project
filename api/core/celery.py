from __future__ import absolute_import

import os
from time import sleep
from celery import Celery


from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local_settings')

from django.conf import settings

app = Celery('core', include=[
    'core.tasks',
    'core.tasks.test_task',
])

app.config_from_object('django.conf:settings')
app.conf.worker_max_memory_per_child = 300000
app.conf.worker_max_tasks_per_child = 10


app.conf.update({'worker_hijack_root_logger': False})

app.autodiscover_tasks()

