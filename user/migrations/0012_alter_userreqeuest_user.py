# Generated by Django 4.2.3 on 2023-07-28 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_userreqeuest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreqeuest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]