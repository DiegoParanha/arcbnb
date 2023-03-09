# Generated by Django 4.1.7 on 2023-03-09 00:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_booking_checkin_alter_booking_checkout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateField(default=datetime.datetime(2023, 3, 9, 0, 4, 44, 739684), verbose_name='Checkin Date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateField(default=datetime.datetime(2023, 3, 9, 0, 4, 44, 739687), verbose_name='Checkout Date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 9, 0, 4, 44, 739674), verbose_name='Booking Date'),
        ),
    ]