# Generated by Django 3.1 on 2021-10-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Placed', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Placed', max_length=10),
        ),
    ]
