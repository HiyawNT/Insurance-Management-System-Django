# Generated by Django 3.0.5 on 2022-08-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_policy',
            name='policy_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
