# Generated by Django 4.2.3 on 2023-08-01 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_profile_is_verified_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_name',
        ),
    ]