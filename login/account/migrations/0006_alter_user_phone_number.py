# Generated by Django 5.0.4 on 2024-05-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Phone_number',
            field=models.IntegerField(),
        ),
    ]