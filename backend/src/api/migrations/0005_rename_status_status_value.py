# Generated by Django 4.1.7 on 2023-04-06 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_status_alter_command_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='status',
            new_name='value',
        ),
    ]
