# Generated by Django 4.1.7 on 2023-06-06 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_recommendation_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation_model',
            name='Search_Words',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]