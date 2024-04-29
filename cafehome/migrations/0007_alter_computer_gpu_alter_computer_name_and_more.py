# Generated by Django 5.0.4 on 2024-04-29 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafehome", "0006_rename_computer_id_transaction_computer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computer",
            name="gpu",
            field=models.CharField(
                blank=True,
                choices=[
                    ("NVIDIA GeForce RTX 3090", "NVIDIA GeForce RTX 3090"),
                    ("NVIDIA GeForce RTX 3080", "NVIDIA GeForce RTX 3080"),
                    ("NVIDIA GeForce RTX 3070", "NVIDIA GeForce RTX 3070"),
                    ("NVIDIA GeForce RTX 3060", "NVIDIA GeForce RTX 3060"),
                    ("AMD Radeon RX 6900 XT", "AMD Radeon RX 6900 XT"),
                    ("AMD Radeon RX 6800 XT", "AMD Radeon RX 6800 XT"),
                    ("AMD Radeon RX 6700 XT", "AMD Radeon RX 6700 XT"),
                ],
                max_length=100,
                null=True,
                verbose_name="Graphics Card",
            ),
        ),
        migrations.AlterField(
            model_name="computer",
            name="name",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                unique=True,
                verbose_name="Computer Name",
            ),
        ),
        migrations.AlterField(
            model_name="computer",
            name="processor",
            field=models.CharField(
                blank=True,
                choices=[
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
                ],
                max_length=100,
                null=True,
                verbose_name="Processor",
            ),
        ),
        migrations.AlterField(
            model_name="computer",
            name="ram",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (2, "2 GB"),
                    (4, "4 GB"),
                    (8, "8 GB"),
                    (16, "16 GB"),
                    (32, "32 GB"),
                    (64, "64 GB"),
                    (128, "128 GB"),
                    (256, "256 GB"),
                ],
                null=True,
                verbose_name="Random Access Memory",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="customer_name",
            field=models.CharField(max_length=100, verbose_name="Customer Name"),
        ),
    ]
