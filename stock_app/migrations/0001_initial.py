# Generated by Django 5.0.6 on 2024-07-12 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                ("name", models.CharField(max_length=255)),
                (
                    "email",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stocks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stock_code", models.CharField(max_length=10)),
                ("sell_at", models.FloatField()),
                ("buy_at", models.FloatField()),
                ("cur_price", models.FloatField()),
                ("time_to_search", models.IntegerField(default="1800000")),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stock_app.person",
                    ),
                ),
            ],
        ),
    ]
