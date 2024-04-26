from django.db import models
from users.models import Customer


# Create your models here.
class Computer(models.Model):
    name = models.CharField(verbose_name="Computer Name",max_length=30,unique=True)
    processor = models.CharField(verbose_name="Processor",max_length=30)
    ram = models.IntegerField(verbose_name="Random Access Memory")
    gpu = models.CharField(verbose_name="Graphics Card",max_length=30)
    wifi = models.BooleanField(verbose_name="WiFi",default=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Computer Detail"
        ordering= ["name"]

    
class Transaction(models.Model):
    customer_id= models.OneToOneField(Customer, on_delete=models.CASCADE)
    customer_name= models.CharField(verbose_name="Customer Name",max_length=30)
    computer_id= models.OneToOneField(Computer, on_delete=models.CASCADE)
    transaction_id= models.IntegerField(verbose_name="Transaction Id")
    transaction_date= models.DateField(verbose_name="Transaction Date")
    transaction_amount= models.IntegerField(verbose_name="Transaction Amount")
    
    def __str__(self):
        return self.customer_name+str(self.transaction_id)
    
    class Meta:
        verbose_name="Transactions Detail"
        ordering= ["transaction_id"]
    