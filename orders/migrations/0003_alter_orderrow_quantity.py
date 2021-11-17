# Generated by Django 3.2.7 on 2021-09-27 07:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210913_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderrow',
            name='quantity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
