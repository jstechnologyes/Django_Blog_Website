# Generated by Django 3.1.5 on 2021-09-07 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_auto_20210907_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link About To Read Blog Post...', max_length=255),
        ),
    ]
