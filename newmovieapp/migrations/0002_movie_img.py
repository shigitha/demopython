# Generated by Django 4.0.4 on 2022-05-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newmovieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='hello', upload_to='gallery'),
            preserve_default=False,
        ),
    ]