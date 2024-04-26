# Generated by Django 5.0.4 on 2024-04-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_customer_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="address",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="age",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="profile",
            field=models.ImageField(null=True, upload_to="media"),
        ),
    ]
