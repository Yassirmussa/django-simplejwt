# Generated by Django 5.0.4 on 2024-05-03 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='user_groups', related_query_name='users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_permissions', related_query_name='users', to='auth.permission')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]