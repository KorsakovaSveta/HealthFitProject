# Generated by Django 5.1.2 on 2024-12-14 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_mealgroups_products_recipes_ingredients_cookingsteps_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfood',
            old_name='user_id',
            new_name='user',
        ),
    ]