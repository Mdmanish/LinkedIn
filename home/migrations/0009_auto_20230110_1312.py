# Generated by Django 2.2 on 2023-01-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20230110_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
