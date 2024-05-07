# -*- coding: utf-8 -*-
# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings

# os.environ.setdefault("DJANGO_SETTING_MODULE", "cafee83.settings")

# app = Celery("cafee83")
# app.conf.update(timezone="Asia/Kolkata")
# app.config_from_object(settings, namespace="CELERY")

# app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f"Request: {self.request!r}")


# celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafee83.settings")

app = Celery("cafee83")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
