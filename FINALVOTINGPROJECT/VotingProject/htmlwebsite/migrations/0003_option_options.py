# Generated by Django 5.0.1 on 2024-03-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0002_rename_option_text_option_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='options',
            field=models.ManyToManyField(related_name='polls', to='htmlwebsite.option'),
        ),
    ]
