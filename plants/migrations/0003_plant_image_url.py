# Generated by Django 5.2 on 2025-04-18 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_carelog'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='image_url',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]
