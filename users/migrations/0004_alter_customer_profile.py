# Generated by Django 5.0.4 on 2024-04-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_customer_address_alter_customer_age_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="profile",
            field=models.ImageField(null=True, upload_to="profile"),
        ),
    ]