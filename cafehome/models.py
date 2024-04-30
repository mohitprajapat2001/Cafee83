from django.db import models
from users.models import Customer

processor_choices = [
    ("Intel Core i9", "Intel Core i9"),
    ("Intel Core i7", "Intel Core i7"),
    ("Intel Core i5", "Intel Core i5"),
    ("AMD Ryzen 9", "AMD Ryzen 9"),
    ("AMD Ryzen 7", "AMD Ryzen 7"),
    ("AMD Ryzen 5", "AMD Ryzen 5"),
    ("Apple M1", "Apple M1"),
    ("Qualcomm Snapdragon", "Qualcomm Snapdragon"),
    ("Samsung Exynos", "Samsung Exynos"),
    ("MediaTek Dimensity", "MediaTek Dimensity"),
]

gpu_choices = [
    ("NVIDIA GeForce RTX 3090", "NVIDIA GeForce RTX 3090"),
    ("NVIDIA GeForce RTX 3080", "NVIDIA GeForce RTX 3080"),
    ("NVIDIA GeForce RTX 3070", "NVIDIA GeForce RTX 3070"),
    ("NVIDIA GeForce RTX 3060", "NVIDIA GeForce RTX 3060"),
    ("AMD Radeon RX 6900 XT", "AMD Radeon RX 6900 XT"),
    ("AMD Radeon RX 6800 XT", "AMD Radeon RX 6800 XT"),
    ("AMD Radeon RX 6700 XT", "AMD Radeon RX 6700 XT"),
]

ram_choices = [
    (2, "2 GB"),
    (4, "4 GB"),
    (8, "8 GB"),
    (16, "16 GB"),
    (32, "32 GB"),
    (64, "64 GB"),
    (128, "128 GB"),
    (256, "256 GB"),
]


# Create your models here.
class Computer(models.Model):
    name = models.CharField(
        verbose_name="Computer Name", max_length=100, unique=True, null=True, blank=True
    )
    processor = models.CharField(
        verbose_name="Processor",
        max_length=100,
        null=True,
        blank=True,
        choices=processor_choices,
    )
    ram = models.IntegerField(
        verbose_name="Random Access Memory", null=True, blank=True, choices=ram_choices
    )
    gpu = models.CharField(
        verbose_name="Graphics Card",
        max_length=100,
        null=True,
        blank=True,
        choices=gpu_choices,
    )
    wifi = models.BooleanField(verbose_name="WiFi", default=True)
    usage_price = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Computer Detail"
        ordering = ["name"]


class Transaction(models.Model):
    customer_name = models.CharField(verbose_name="Customer Name", max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    transaction_id = models.CharField(verbose_name="Transaction Id")
    transaction_date = models.DateTimeField(verbose_name="Transaction Date")
    transaction_amount = models.FloatField(verbose_name="Transaction Amount")

    def __str__(self):
        return self.customer_name + " " + str(self.transaction_id)

    class Meta:
        verbose_name = "Transactions Detail"
        ordering = ["transaction_id"]
