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
    list_display = ["customer", "transaction_date", "transaction_id"]
    fieldsets = [
        ("Customer Details", {
            "fields": ["customer", "payer_username"]
        }),
        ("Computer Details", {
            "fields": ["computer"]
        }),
        ("Transaction Details", {
            "fields": ["transaction_id","transaction_amount", "transaction_date"]
        }),
    ]
    ordering = ["transaction_id"]
    search_fields = ["payer_username", "transaction_id"]
    list_filter = ["customer__username", "transaction_date"] 
    

    