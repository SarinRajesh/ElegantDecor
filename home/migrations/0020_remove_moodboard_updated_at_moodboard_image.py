# Generated by Django 5.0.6 on 2024-10-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_moodboard_moodboarditem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodboard',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='moodboard',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mood_boards/'),
        ),
    ]
