# Generated by Django 4.2.3 on 2023-08-05 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="renter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Арендатор",
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reservations",
                to="orders.reservationstatus",
                verbose_name="Статус резервирования",
            ),
        ),
    ]
