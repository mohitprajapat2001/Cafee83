from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    profile= models.ImageField(upload_to="media", null=True)
    age= models.IntegerField(null=True)
    address= models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    
    def __str__(self):
        return self.username