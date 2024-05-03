# -*- coding: utf-8 -*-
from django.db import models
from users.models import Customer
from .choices import GPU_CHOICES, PROCESSOR_CHOICES, RAM_CHOICES


# Create your models here.
class Computer(models.Model):
    name = models.CharField(
        verbose_name="Computer Name", max_length=100, unique=True, null=True, blank=True
    )
    processor = models.CharField(
        default="INTEL_I5",
        verbose_name="Processor",
        max_length=100,
        choices=PROCESSOR_CHOICES,
    )
    ram = models.IntegerField(
        default=2, verbose_name="Random Access Memory", choices=RAM_CHOICES
    )
    gpu = models.CharField(
        verbose_name="Graphics Card",
        max_length=100,
        null=True,
        blank=True,
        choices=GPU_CHOICES,
    )
    wifi = models.BooleanField(verbose_name="WiFi", default=True)
    usage_price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Computer Detail"
        ordering = ["name"]


class Transaction(models.Model):
    payer_username = models.CharField(verbose_name="Payer Name", max_length=100)
    customer_details = models.ForeignKey(Customer, on_delete=models.CASCADE)
    computer_details = models.ForeignKey(Computer, on_delete=models.CASCADE)
    transaction_id = models.CharField(verbose_name="Transaction Id")
    transaction_amount = models.FloatField(verbose_name="Transaction Amount")
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payer_username + " " + str(self.transaction_id)

    class Meta:
        verbose_name = "Transactions Detail"
        ordering = ["transaction_id"]
