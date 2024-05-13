# -*- coding: utf-8 -*-
import os
from celery import Celery
from datetime import timedelta


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafee83.settings")

app = Celery("cafee83")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
