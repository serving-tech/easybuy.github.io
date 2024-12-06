# Generated by Django 5.0.7 on 2024-12-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='map_url',
            field=models.URLField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='video_url',
            field=models.URLField(blank=True, max_length=600, null=True),
        ),
    ]