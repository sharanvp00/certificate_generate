# Generated by Django 4.2 on 2025-04-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
