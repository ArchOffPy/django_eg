# Generated by Django 5.1.7 on 2025-03-22 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'United States Dollar'), ('RUB', 'Russian Rub')], default='RUB', max_length=3),
        ),
    ]
