# Generated by Django 2.2.11 on 2020-03-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200318_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_link',
            field=models.URLField(max_length=500),
        ),
    ]