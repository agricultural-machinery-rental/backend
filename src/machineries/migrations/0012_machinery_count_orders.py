# Generated by Django 4.2.3 on 2023-09-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "machineries",
            "0011_alter_machinery_options_alter_machinery_location_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="machinery",
            name="count_orders",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Количество заказов"
            ),
        ),
    ]