# Generated by Django 4.0.3 on 2022-04-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(default='N/A', max_length=30),
        ),
    ]
