# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from users.models import Customer
import cafee83.choice as choice
from cafee83.choiceconstant import INTEL_CORE_I5, NVIDIA_GEFORCE_RTX_3060, TWO


class Computer(ActivatorModel):
    name = models.CharField(
        verbose_name="Computer Name", max_length=100, unique=True, null=True, blank=True
    )
    processor = models.CharField(
        verbose_name="Processor",
        default=INTEL_CORE_I5,
        max_length=100,
        choices=choice.PROCESSORCHOICES,
    )
    ram = models.CharField(
        verbose_name="Random Access Memory",
        max_length=10,
        default=TWO,
        choices=choice.RAMCHOICES,
    )
    gpu = models.CharField(
        verbose_name="Graphics Card",
        max_length=100,
        null=True,
        blank=True,
        choices=choice.GPUCHOICES,
        default=NVIDIA_GEFORCE_RTX_3060,
    )
    wifi = models.BooleanField(verbose_name="WiFi", default=True)
    usage_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Computer Details"
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

    def __str__(self):
        return "Transaction By {name} : {id} of RS {amount}".format(
            name=self.payer_username,
            id=self.transaction_id,
            amount=self.transaction_amount,
        )

    class Meta:
        verbose_name = "Transactions Detail"
        ordering = ["-created"]
