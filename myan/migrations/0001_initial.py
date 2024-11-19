# Generated by Django 5.1.1 on 2024-11-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('audio', models.FileField(upload_to='audio/')),
                ('cover', models.ImageField(upload_to='images/')),
                ('duration', models.PositiveIntegerField(default=0, help_text='Duration in seconds')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('songs', models.ManyToManyField(to='myan.song')),
            ],
        ),
    ]
