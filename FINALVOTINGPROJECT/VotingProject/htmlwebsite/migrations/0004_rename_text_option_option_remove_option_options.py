# Generated by Django 5.0.1 on 2024-03-26 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0003_option_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='text',
            new_name='option',
        ),
        migrations.RemoveField(
            model_name='option',
            name='options',
        ),
    ]
