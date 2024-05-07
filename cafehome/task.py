# -*- coding: utf-8 -*-
from celery import shared_task


@shared_task(bind=True)
def update_computer_status(self):
    print("I am Here")
    return "Done"
