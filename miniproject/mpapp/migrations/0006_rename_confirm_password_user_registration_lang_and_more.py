# Generated by Django 4.1.7 on 2023-04-23 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpapp', '0005_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_registration',
            old_name='confirm_password',
            new_name='lang',
        ),
        migrations.RenameField(
            model_name='user_registration',
            old_name='full_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user_registration',
            old_name='language',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='user_registration',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='user_registration',
            name='gender',
        ),
    ]
