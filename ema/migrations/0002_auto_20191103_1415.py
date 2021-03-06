# Generated by Django 2.2.4 on 2019-11-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ema', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='food',
            new_name='fatigue',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='physical_activity',
            new_name='interest',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='sleep_hour',
            new_name='restlessness',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='sleep_minute',
            new_name='sleep',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='social_activity',
            new_name='suicide',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='stress',
            new_name='weight',
        ),
        migrations.AddField(
            model_name='response',
            name='worthlessness',
            field=models.SmallIntegerField(default=-1),
        ),
    ]
