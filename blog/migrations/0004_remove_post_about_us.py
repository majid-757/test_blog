# Generated by Django 3.2.10 on 2022-05-15 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_about_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='about_us',
        ),
    ]
