# Generated by Django 4.2.1 on 2023-05-08 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagesapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='Mobile_Number',
        ),
    ]
