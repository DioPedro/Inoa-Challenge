# Generated by Django 5.0.6 on 2024-07-15 17:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock_app", "0005_alter_stocks_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stocks",
            name="time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]