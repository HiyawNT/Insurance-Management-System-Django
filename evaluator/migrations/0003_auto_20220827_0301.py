# Generated by Django 3.0.5 on 2022-08-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0002_auto_20220823_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluator',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/Evaluator/'),
        ),
    ]
