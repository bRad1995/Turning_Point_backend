# Generated by Django 4.2.10 on 2024-02-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmember',
            name='image',
            field=models.CharField(default='Upload Image URL', max_length=500),
        ),
    ]