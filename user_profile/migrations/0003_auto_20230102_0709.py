# Generated by Django 2.2 on 2023-01-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20230102_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='amir.jpg', upload_to='profile_pic'),
        ),
    ]