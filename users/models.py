from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Customer(AbstractUser):
    profile = models.ImageField(
        upload_to="Customer_Profile",
        default="default/profile2.png",
        null=True,
        blank=True
    )
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
