# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Customer


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["username", "is_staff", "is_active"]
    fieldsets = [
        (
            "Customer Details",
            {
                "fields": [
                    "profile",
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password",
                    "age",
                    "address",
                    "phone",
                ]
            },
        ),
        ("Status Details", {"fields": ["is_staff", "is_superuser", "is_active"]}),
        ("Login Details", {"fields": ["date_joined", "last_login"]}),
        ("Group Details", {"fields": ["groups", "user_permissions"]}),
    ]
    search_fields = ["username"]
    list_filter = ["is_staff", "is_active", "is_superuser"]
    ordering = ["username"]
