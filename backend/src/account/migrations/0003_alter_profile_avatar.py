# Generated by Django 4.1.7 on 2023-03-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_coins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
