# Generated by Django 5.0.6 on 2024-06-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
