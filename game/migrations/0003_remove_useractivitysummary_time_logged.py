# Generated by Django 3.2.7 on 2021-09-14 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20210914_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivitysummary',
            name='time_logged',
        ),
    ]