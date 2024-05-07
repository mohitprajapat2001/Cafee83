# -*- coding: utf-8 -*-
from celery import shared_task


@shared_task
def activate_computer(computer_id):
    for i in range(100000):
        if i == 99999:
            print(i)
    return "done"
