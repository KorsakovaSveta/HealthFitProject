# Generated by Django 5.1.2 on 2024-11-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_exercise_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutexercise',
            name='calories',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]