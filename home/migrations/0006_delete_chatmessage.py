# Generated by Django 5.0.6 on 2024-09-01 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_chatmessage_related_design'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]