# Generated by Django 5.0.3 on 2024-04-03 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booking",
            options={"ordering": ("booking_date",)},
        ),
        migrations.AlterModelOptions(
            name="menu",
            options={"ordering": ("title",)},
        ),
    ]