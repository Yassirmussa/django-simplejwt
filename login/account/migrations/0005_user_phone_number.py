# Generated by Django 5.0.4 on 2024-05-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_rid_user_gender_delete_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Phone_number',
            field=models.IntegerField(default=111, max_length=10),
            preserve_default=False,
        ),
    ]
