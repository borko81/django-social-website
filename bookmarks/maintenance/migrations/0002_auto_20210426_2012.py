# Generated by Django 3.2 on 2021-04-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='date_solve',
            field=models.DateTimeField(blank=True),
        ),
    ]
