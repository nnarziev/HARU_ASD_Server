# Generated by Django 2.2.4 on 2019-10-28 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20191028_2338'),
        ('sensor_data', '0005_app_usage_stats'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='app_usage_stats',
            unique_together={('username', 'package_name', 'start_timestamp')},
        ),
    ]
