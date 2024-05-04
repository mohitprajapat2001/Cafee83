# -*- coding: utf-8 -*-
from django.db import models
from users.models import Customer
import cafehome.choice as choice

print(choice.GPUCHOICES[0])


# Create your models here.
class Computer(models.Model):
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
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Computer Details"
        ordering = ["name"]


class Transaction(models.Model):
    payer_username = models.CharField(verbose_name="Payer Name", max_length=100)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customers"
    )
    computer = models.ForeignKey(
        Computer, on_delete=models.CASCADE, related_name="computers"
    )
    transaction_id = models.CharField(verbose_name="Transaction Id")
    transaction_amount = models.FloatField(verbose_name="Transaction Amount")
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payer_username + " " + str(self.transaction_id)

    class Meta:
        verbose_name = "Transactions Detail"
        ordering = ["transaction_id"]
