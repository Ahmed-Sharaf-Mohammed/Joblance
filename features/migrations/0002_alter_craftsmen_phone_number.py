# Generated by Django 4.1.7 on 2023-04-21 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craftsmen',
            name='phone_number',
            field=models.IntegerField(default='none'),
        ),
    ]