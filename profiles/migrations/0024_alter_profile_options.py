# Generated by Django 4.1.7 on 2023-06-01 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-id']},
        ),
    ]
