# Generated by Django 3.0.5 on 2022-08-10 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20220810_0732'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BankNameLists',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
