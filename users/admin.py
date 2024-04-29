from django.contrib import admin
from .models import Customer
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', "username", "is_staff", "is_active"]
    fieldsets = [
        ("Customer Details", {
            "fields": ["first_name", "last_name", "username", "email", "password", "age", "address", "phone"]
        }),
        ("Status Details", {
            "fields": ["is_staff", "is_superuser", "is_active"]
        }),
        ("Login Details", {
            "fields": ["date_joined", "last_login"]
        }),
        ("Group Details", {
            "fields": ["groups", "user_permissions"]
        }),
    ]
    search_fields= ["username"]
    list_filter=["is_staff", "is_active", "is_superuser"]
