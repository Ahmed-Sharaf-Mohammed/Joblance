# Generated by Django 4.1.7 on 2023-05-14 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_alter_profile_options_profile_face_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='RAting',
        ),
        migrations.AddField(
            model_name='rate',
            name='RAtingMoralistic',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='rate',
            name='RAtingQuality',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='rate',
            name='RAtingSpeed',
            field=models.IntegerField(default='0'),
        ),
    ]
