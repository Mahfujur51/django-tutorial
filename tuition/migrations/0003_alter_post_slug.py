# Generated by Django 4.0.3 on 2022-04-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default=models.CharField(max_length=100), max_length=100),
        ),
    ]
