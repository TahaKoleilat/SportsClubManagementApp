# Generated by Django 3.0 on 2022-04-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_auto_20220409_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.CharField(max_length=100),
        ),
    ]
