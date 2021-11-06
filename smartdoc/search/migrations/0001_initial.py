# Generated by Django 3.1.4 on 2021-04-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='title', max_length=50)),
                ('audio_file', models.FileField(upload_to='uploads/audio')),
                ('text', models.CharField(blank=True, default='audio text', max_length=5000)),
            ],
            options={
                'db_table': 'audio',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='title', max_length=50)),
                ('image_file', models.ImageField(upload_to='uploads/images')),
                ('text', models.CharField(blank=True, default='image text', max_length=5000)),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
