# Generated by Django 4.1.1 on 2022-09-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stripepay", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="name_stripe",
            field=models.CharField(default="", max_length=100),
        ),
    ]
