# Generated by Django 5.0.4 on 2024-05-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafehome", "0004_rename_computer_transaction_computer_details_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
