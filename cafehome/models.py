# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from users.models import Customer
import cafee83.choice as choice
from cafee83 import choiceconstant
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import tasks
from django.utils import timezone
from datetime import timedelta


class Computer(ActivatorModel):
    name = models.CharField(
        verbose_name="Computer Name", max_length=100, unique=True, null=True, blank=True
    )
    processor = models.CharField(
        verbose_name="Processor",
        default=choiceconstant.INTEL_CORE_I5,
        max_length=100,
        choices=choice.PROCESSORCHOICES,
    )
    ram = models.CharField(
        verbose_name="Random Access Memory",
        max_length=10,
        default=choiceconstant.TWO,
        choices=choice.RAMCHOICES,
    )
    gpu = models.CharField(
        verbose_name="Graphics Card",
        max_length=100,
        null=True,
        blank=True,
        choices=choice.GPUCHOICES,
        default=choiceconstant.NVIDIA_GEFORCE_RTX_3060,
    )
    wifi = models.BooleanField(verbose_name="WiFi", default=True)
    usage_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Computer Detail"
        ordering = ["name"]


class Transaction(TimeStampedModel):
    payer_username = models.CharField(verbose_name="Payer Name", max_length=100)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="transactions"
    )
    computer = models.ForeignKey(
        Computer, on_delete=models.CASCADE, related_name="transactions"
    )
    transaction_id = models.CharField(verbose_name="Transaction Id")
    transaction_amount = models.FloatField(verbose_name="Transaction Amount")
    transaction_status = models.CharField(
        verbose_name="Transaction Status", max_length=10
    )

    def __str__(self):
        return "Transaction By {name} : {id} of RS {amount}".format(
            name=self.payer_username,
            id=self.transaction_id,
            amount=self.transaction_amount,
        )

    class Meta:
        verbose_name = "Transactions Detail"
        ordering = ["-created"]


@receiver(post_save, sender=Transaction)
def update_computer_status(sender, instance, created, **kwargs):
    if created:
        computer = instance.computer
        computer.status = 0
        computer.save()
        activation_time = (timezone.now() + timedelta(minutes=1)) - timezone.now()
        # tasks.activate_computer.apply_async(args=[computer.id], eta=activation_time)
        tasks.activate_computer.apply_async(
            args=[computer.id], countdown=activation_time.total_seconds()
        )
