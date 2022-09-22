# Generated by Django 4.0.6 on 2022-08-29 15:50

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=14, verbose_name='name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
                ('likes', models.IntegerField(blank=True, default=0, verbose_name='likes')),
                ('image', cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
