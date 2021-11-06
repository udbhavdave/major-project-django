# Generated by Django 3.2 on 2021-05-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(upload_to='uploads/audio', verbose_name='audio_file'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='text',
            field=models.TextField(blank=True, default='', verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='title',
            field=models.CharField(blank=True, default='title', max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='uploads/images', verbose_name='image_file'),
        ),
        migrations.AlterField(
            model_name='image',
            name='text',
            field=models.TextField(blank=True, default='', verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, default='title', max_length=100, verbose_name='title'),
        ),
    ]
