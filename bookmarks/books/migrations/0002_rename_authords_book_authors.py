# Generated by Django 3.2 on 2021-04-19 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authords',
            new_name='authors',
        ),
    ]
