# Generated by Django 4.1.7 on 2023-03-11 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('SA$', 'SA$'), ('SC$', 'SC$')], default='SC$', max_length=9),
        ),
    ]
