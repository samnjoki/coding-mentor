# Generated by Django 4.2.7 on 2023-11-15 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorclub', '0007_remove_mentor_fields_remove_mentor_users_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lastname',
        ),
    ]