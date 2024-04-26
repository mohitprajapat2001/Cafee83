from django.contrib import admin
from .models import Computer,Transaction

# Register your models here.

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    fieldsets= [
        ("Computer Details", {
            "fields": ["name", "processor", "ram", "gpu", "wifi", "is_active"]
        })]
    list_display= ["name","processor","ram","gpu"]
    ordering= ["name"]
    search_fields= ["name"]
    list_filter=["name", "ram", "is_active"]
    actions= ["set_unactive"]
    
    @admin.action(description="Mark selected Computers as Unactive")
    def set_unactive(self, queryset):
        queryset.update(is_active=False)
    

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display= ["customer_name", "transaction_date", "transaction_id"]
    fieldsets= [
        ("Customer Details", {
            "fields": ["customer_id","customer_name"]
        }),
        ("Computer Details", {
            "fields": ["computer_id"]
        }),
        ("Transaction Details", {
            "fields": ["transaction_id","transaction_amount", "transaction_date"]
        }),
    ]
    ordering= ["transaction_id"]
    search_fields= ["customer_name", "transaction_id"]
    list_filter=["customer_name", "transaction_date"]
    

    