# Generated by Django 4.2.1 on 2023-05-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_Created_By', models.CharField(max_length=62322222222222222)),
                ('Marital_Status', models.CharField(max_length=62322222222222222)),
                ('Your_Religion', models.CharField(max_length=62322222222222222)),
                ('Your_Caste', models.CharField(max_length=62322222222222222)),
                ('Sub_Caste', models.CharField(max_length=62322222222222222)),
                ('About_Yourself', models.CharField(max_length=62322222222222222)),
                ('Name', models.CharField(max_length=444444)),
                ('Surname', models.CharField(max_length=4444444)),
                ('Email', models.EmailField(max_length=444444)),
                ('Gender', models.CharField(max_length=44444)),
                ('D_O_B', models.CharField(max_length=44444)),
                ('Mobile_Number', models.CharField(max_length=444444)),
                ('Height', models.CharField(max_length=444444)),
                ('Blood_Group', models.CharField(max_length=444444)),
                ('Age', models.CharField(max_length=444444)),
            ],
        ),
    ]
