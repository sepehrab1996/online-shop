# Generated by Django 3.2.8 on 2021-11-22 15:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 18, 55, 14, 29286, tzinfo=utc), verbose_name='order date'),
        ),
    ]
