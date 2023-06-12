# Generated by Django 4.2 on 2023-06-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onestopsalon', '0008_alter_salon_close_alter_salon_open'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salon',
            name='close',
        ),
        migrations.RemoveField(
            model_name='salon',
            name='open',
        ),
        migrations.AddField(
            model_name='salon',
            name='close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salon',
            name='open_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
