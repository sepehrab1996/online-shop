# Generated by Django 3.2.7 on 2021-09-13 08:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20210913_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=20),
        ),
    ]
