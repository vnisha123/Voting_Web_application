# Generated by Django 5.0.1 on 2024-04-02 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0006_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
