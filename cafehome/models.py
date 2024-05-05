# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.models import ActivatorModel
from users.models import Customer
import cafehome.choice as choice


class Computer(ActivatorModel):
    name = models.CharField(
        verbose_name="Computer Name", max_length=100, unique=True, null=True, blank=True
    )
    processor = models.CharField(
        default=choice.PROCESSORCHOICES[0],
        verbose_name="Processor",
        max_length=100,
        choices=choice.PROCESSORCHOICES,
    )
    ram = models.IntegerField(
        default=choice.RAMCHOICES[0],
        verbose_name="Random Access Memory",
        choices=choice.RAMCHOICES,
    )
    gpu = models.CharField(
        verbose_name="Graphics Card",
        max_length=100,
        null=True,
        blank=True,
        choices=choice.GPUCHOICES,
        default=choice.GPUCHOICES[0],
    )
    wifi = models.BooleanField(verbose_name="WiFi", default=True)
    usage_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Computer Details"
        ordering = ["name"]


class Transaction(models.Model):
    payer_username = models.CharField(verbose_name="Payer Name", max_length=100)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="transactions"
    )
    computer = models.ForeignKey(
        Computer, on_delete=models.CASCADE, related_name="transactions"
    )
    transaction_id = models.CharField(verbose_name="Transaction Id")
    transaction_amount = models.FloatField(verbose_name="Transaction Amount")
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Transaction By {name} : {id} of RS {amount}".format(
            name=self.payer_username,
            id=self.transaction_id,
            amount=self.transaction_amount,
        )

    class Meta:
        verbose_name = "Transactions Detail"
        ordering = ["-transaction_date"]
