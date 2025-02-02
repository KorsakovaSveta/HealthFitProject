# Generated by Django 5.1.2 on 2024-11-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_workoutexercise_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='demonstration_video_2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='equipment',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='demonstration_video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
