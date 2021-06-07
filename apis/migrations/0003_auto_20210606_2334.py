# Generated by Django 3.2.3 on 2021-06-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20210606_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='photosubmission',
            field=models.ImageField(default='random', max_length=200, upload_to='pic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='attendance',
            field=models.BooleanField(default=False),
        ),
    ]
