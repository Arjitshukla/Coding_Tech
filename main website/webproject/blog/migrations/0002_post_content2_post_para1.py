# Generated by Django 4.2.6 on 2024-01-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Content2',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='para1',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]