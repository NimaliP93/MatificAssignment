# Generated by Django 3.2.7 on 2021-09-14 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_useractivitysummary_activity_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useractivitysummary',
            old_name='activity_time',
            new_name='time_duration',
        ),
        migrations.RemoveField(
            model_name='useractivitysummary',
            name='online_status',
        ),
        migrations.AddField(
            model_name='useractivitysummary',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
