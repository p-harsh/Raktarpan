# Generated by Django 3.2.12 on 2023-04-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20230417_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationcertificate',
            name='signature',
            field=models.CharField(max_length=30),
        ),
    ]
