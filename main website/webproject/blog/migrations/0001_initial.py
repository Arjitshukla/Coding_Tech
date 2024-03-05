# Generated by Django 4.2.6 on 2024-01-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=13)),
                ('Content', models.TextField()),
                ('head0', models.CharField(max_length=50)),
                ('para0', models.TextField()),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('slug', models.CharField(max_length=150)),
                ('image', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
