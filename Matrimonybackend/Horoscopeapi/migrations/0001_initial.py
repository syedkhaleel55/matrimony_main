# Generated by Django 4.2.1 on 2023-05-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horoscope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Moon_Sign', models.CharField(max_length=150)),
                ('Star', models.CharField(max_length=150)),
                ('Hororscope_Match', models.CharField(max_length=150)),
                ('Manglik', models.CharField(max_length=150)),
                ('Shani', models.CharField(max_length=150)),
                ('Gotra', models.CharField(max_length=150)),
                ('Place_Of_Birth', models.CharField(max_length=150)),
                ('Place_Of_Country', models.CharField(max_length=150)),
                ('Hours', models.CharField(max_length=232222)),
                ('Minitues', models.CharField(max_length=232222)),
                ('Seconds', models.CharField(max_length=232222)),
                ('Am_Pm', models.CharField(max_length=232222)),
            ],
        ),
    ]