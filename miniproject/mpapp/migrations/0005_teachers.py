# Generated by Django 4.1.7 on 2023-04-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpapp', '0004_langs'),
    ]

    operations = [
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lang', models.CharField(max_length=250)),
                ('prof', models.CharField(max_length=250)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
