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
    actions = ["Active_Computers"]

    @admin.action(description="Mark selected computers active")
    def Active_Computers(self, request, queryset):
        queryset.update(status=1)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["customer", "created", "transaction_id", "transaction_status"]
    fieldsets = [
        ("Customer Details", {"fields": ["customer", "payer_username"]}),
        ("Computer Details", {"fields": ["computer"]}),
        (
            "Transaction Details",
            {"fields": ["transaction_id", "transaction_amount", "transaction_status"]},
        ),
    ]
    ordering = ["transaction_id"]
    search_fields = ["payer_username", "transaction_id"]
    list_filter = ["payer_username", "created"]
