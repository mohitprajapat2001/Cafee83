# -*- coding: utf-8 -*-
from celery import shared_task
from . import models


@shared_task(name="activate_computer")
def activate_computer(computer_id):
    computer = models.Computer.objects.get(id=computer_id)
    computer.status = 1
    computer.save()
    return f"Done Status Updated {computer} of ID {computer_id} with Status {computer.status}"
