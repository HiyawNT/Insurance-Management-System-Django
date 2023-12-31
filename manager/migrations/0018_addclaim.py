# Generated by Django 3.0.5 on 2022-08-26 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_auto_20220826_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_name', models.CharField(max_length=200)),
                ('creation_date', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Category')),
            ],
        ),
    ]
