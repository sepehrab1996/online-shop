# Generated by Django 3.2.8 on 2021-11-22 14:56

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Order item',
                'verbose_name_plural': 'Order items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField(default=datetime.datetime(2021, 11, 24, 18, 26, 7, 318028, tzinfo=utc), verbose_name='order date')),
                ('status', models.CharField(choices=[('0', 'ready to send'), ('1', 'sending'), ('2', 'delivered')], default='0', max_length=50, verbose_name='status')),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='discount')),
                ('final_price', models.PositiveIntegerField(verbose_name='final price')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.address', verbose_name='address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='costumer')),
                ('items', models.ManyToManyField(to='orders.OrderItem', verbose_name='items')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='discount code')),
                ('valid_from', models.DateTimeField(verbose_name='valid from')),
                ('valid_to', models.DateTimeField(verbose_name='valid to')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='discount')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='customer.customer', verbose_name='owner')),
            ],
            options={
                'verbose_name': 'Discount code',
                'verbose_name_plural': 'Discount codes',
            },
        ),
    ]
