# Generated by Django 4.2.2 on 2023-07-02 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.ImageField(default=0, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('stock_status', models.SmallIntegerField(choices=[(0, 'In stock'), (1, 'Out of stock'), (2, 'Coming Soon')], default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.category')),
            ],
        ),
    ]
