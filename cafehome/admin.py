# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Computer, Transaction

# Register your models here.


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Computer Details",
            {
                "fields": [
                    "name",
                    "processor",
                    "ram",
                    "gpu",
                    "usage_price",
                    "wifi",
                    "status",
                ]
            },
        )
    ]
    list_display = ["name", "processor", "ram", "gpu"]
    ordering = ["name"]
    search_fields = ["name"]
    list_filter = ["name", "ram", "status"]

    @admin.action(description="Mark selected Computers as Unactive")
    def set_unactive(self, queryset):
        queryset.update(status=False)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["customer", "transaction_date", "transaction_id"]
    fieldsets = [
        ("Customer Details", {"fields": ["customer", "payer_username"]}),
        ("Computer Details", {"fields": ["computer"]}),
        (
            "Transaction Details",
            {"fields": ["transaction_id", "transaction_amount"]},
        ),
    ]
    ordering = ["transaction_id"]
    search_fields = ["payer_username", "transaction_id"]
    list_filter = ["payer_username", "transaction_date"]
