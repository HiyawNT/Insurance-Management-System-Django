# Generated by Django 3.0.5 on 2022-08-26 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0019_auto_20220827_0137'),
        ('customer', '0008_auto_20220810_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankNameLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.BigIntegerField()),
                ('payment_amount', models.PositiveIntegerField(null=True)),
                ('transaction_id', models.CharField(max_length=60)),
                ('payment_proof', models.ImageField(blank=True, null=True, upload_to='payments/receipts/')),
                ('payed_date', models.DateField(auto_now=True)),
                ('bank_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.BankNameLists')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Category')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]