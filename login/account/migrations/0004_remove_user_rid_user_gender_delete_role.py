# Generated by Django 5.0.4 on 2024-05-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_role_user_rid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='RID',
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
