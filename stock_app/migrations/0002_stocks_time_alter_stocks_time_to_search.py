# Generated by Django 5.0.6 on 2024-07-14 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="stocks",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 7, 14, 22, 54, 11, 333935)
            ),
        ),
        migrations.AlterField(
            model_name="stocks",
            name="time_to_search",
            field=models.IntegerField(),
        ),
    ]