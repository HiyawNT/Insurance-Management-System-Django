# Generated by Django 3.0.5 on 2022-08-18 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20220810_0931'),
        ('manager', '0007_auto_20220818_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_policy',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
    ]