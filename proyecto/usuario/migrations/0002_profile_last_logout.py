# Generated by Django 4.0 on 2023-04-26 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_logout',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
