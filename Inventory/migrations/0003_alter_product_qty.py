# Generated by Django 4.2.2 on 2023-07-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]
