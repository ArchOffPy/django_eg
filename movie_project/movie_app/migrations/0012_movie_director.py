# Generated by Django 5.1.7 on 2025-04-03 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0011_remove_movie_director_remove_movie_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movie_app.director'),
        ),
    ]
