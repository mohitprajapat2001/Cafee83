# -*- coding: utf-8 -*-
from celery import shared_task


def activate_computer():
    for i in range(100):
        print(i)
    return "done"
