# Generated by Django 4.0 on 2023-04-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/default_profile_image.png', upload_to='profiles/'),
        ),
    ]