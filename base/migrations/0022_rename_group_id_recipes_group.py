# Generated by Django 5.1.2 on 2024-12-14 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_rename_user_id_userfood_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='group_id',
            new_name='group',
        ),
    ]
