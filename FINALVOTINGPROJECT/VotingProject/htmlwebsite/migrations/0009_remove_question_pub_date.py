# Generated by Django 5.0.1 on 2024-04-02 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0008_question_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
    ]
