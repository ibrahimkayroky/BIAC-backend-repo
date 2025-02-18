# Generated by Django 5.0.6 on 2024-06-04 23:08

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_image',
            field=models.ImageField(null=True, upload_to=users.models.upload_to),
        ),
    ]
