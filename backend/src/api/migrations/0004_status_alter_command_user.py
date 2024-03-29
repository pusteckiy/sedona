# Generated by Django 4.1.7 on 2023-04-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_command_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='command',
            name='user',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
