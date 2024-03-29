# Generated by Django 2.2 on 2023-01-05 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0014_auto_20230105_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='details',
        ),
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(default='company', max_length=200),
        ),
        migrations.AddField(
            model_name='experience',
            name='discription',
            field=models.TextField(default='discription'),
        ),
        migrations.AddField(
            model_name='experience',
            name='duration',
            field=models.CharField(default='2.5 years', max_length=200),
        ),
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.ImageField(default='profile_pic/default_exp_img.png', upload_to='profile_pic'),
        ),
        migrations.AddField(
            model_name='experience',
            name='job_type',
            field=models.CharField(default='full-time', max_length=200),
        ),
        migrations.AddField(
            model_name='experience',
            name='joining_date',
            field=models.CharField(default='Jan 2021', max_length=200),
        ),
        migrations.AddField(
            model_name='experience',
            name='leaving_date',
            field=models.CharField(default='Present', max_length=200),
        ),
        migrations.AddField(
            model_name='experience',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]
