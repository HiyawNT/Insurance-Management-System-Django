# Generated by Django 3.0.5 on 2022-08-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_vehicle_policy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='admin_comment',
            new_name='manager_comment',
        ),
    ]
