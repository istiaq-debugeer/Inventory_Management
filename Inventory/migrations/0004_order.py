# Generated by Django 4.2.2 on 2023-07-04 18:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_alter_product_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(default=uuid.uuid4, max_length=100, unique=True)),
                ('qty', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('vat', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.product')),
            ],
        ),
    ]