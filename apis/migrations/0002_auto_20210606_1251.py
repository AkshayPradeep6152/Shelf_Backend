# Generated by Django 3.2.3 on 2021-06-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='reg_start_date',
            new_name='reg_open_date',
        ),
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ImageField(upload_to='uploads/events'),
        ),
    ]
