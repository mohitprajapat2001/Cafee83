from django.db import models


# Create your models here.
class Computer(models.Model):
    name = models.CharField(max_length=30,unique=True)
    processor = models.CharField(max_length=30)
    ram = models.IntegerField()
    gpu = models.CharField(max_length=30)
    wifi = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    