# Generated by Django 2.2 on 2023-01-06 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0025_languages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificates',
            name='details',
        ),
        migrations.AddField(
            model_name='certificates',
            name='expiry_date',
            field=models.CharField(default='No Expiration Date', max_length=200),
        ),
        migrations.AddField(
            model_name='certificates',
            name='image',
            field=models.ImageField(default='profile_pic/default_cover_pic.jpeg', upload_to='profile_pic'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='issue_date',
            field=models.CharField(default='Jan 2021', max_length=200),
        ),
        migrations.AddField(
            model_name='certificates',
            name='organisation',
            field=models.CharField(default='organisation', max_length=200),
        ),
        migrations.AddField(
            model_name='certificates',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
