# Generated by Django 5.1.7 on 2025-03-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_best_selling',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
