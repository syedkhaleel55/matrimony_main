# Generated by Django 4.2.1 on 2023-05-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familydetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Family_Values', models.CharField(max_length=150)),
                ('Family_Type', models.CharField(max_length=150)),
                ('Family_Status', models.CharField(max_length=150)),
                ('No_Of_Brothers', models.CharField(default='null', max_length=150)),
                ('No_Of_Brothers_Married', models.CharField(default='null', max_length=150)),
                ('No_Of_Sisters', models.CharField(default='null', max_length=150)),
                ('No_Of_Sisters_Married', models.CharField(default='null', max_length=150)),
                ('Mother_Tounge', models.CharField(max_length=150)),
                ('Father_Name', models.CharField(default='null', max_length=150)),
                ('Father_Occupation', models.CharField(default='null', max_length=150)),
                ('Mother_Name', models.CharField(default='null', max_length=150)),
                ('Mother_Occupation', models.CharField(default='null', max_length=150)),
                ('Family_wealth', models.CharField(default='null', max_length=150)),
                ('Relative_info', models.CharField(default='null', max_length=150)),
                ('About_Family', models.CharField(max_length=150)),
            ],
        ),
    ]
