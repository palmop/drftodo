# Generated by Django 4.0.3 on 2022-04-05 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_alter_userapp_is_active_alter_userapp_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapp',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
