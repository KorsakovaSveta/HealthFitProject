# Generated by Django 5.1.2 on 2024-11-11 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='calories',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
