# Generated by Django 5.1.2 on 2024-11-20 19:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_workout_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='difficulty_level',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
