# Generated by Django 2.2.4 on 2019-10-26 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.SmallIntegerField(default=None)),
                ('ema_order', models.SmallIntegerField(default=None)),
                ('mood', models.SmallIntegerField(default=-1)),
                ('sleep_hour', models.SmallIntegerField(default=-1)),
                ('sleep_minute', models.SmallIntegerField(default=-1)),
                ('food', models.SmallIntegerField(default=-1)),
                ('physical_activity', models.SmallIntegerField(default=-1)),
                ('social_activity', models.SmallIntegerField(default=-1)),
                ('stress', models.SmallIntegerField(default=-1)),
                ('time_expected', models.BigIntegerField(default=0)),
                ('time_responded', models.BigIntegerField(default=0)),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.Participant')),
            ],
        ),
    ]
