# Generated by Django 2.2.4 on 2019-10-30 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20191029_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='heartbeat_smartphone',
            field=models.BigIntegerField(default=1572399236.746786),
        ),
        migrations.AlterField(
            model_name='participant',
            name='heartbeat_smartwatch',
            field=models.BigIntegerField(default=1572399236.746786),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_ds_smartphone',
            field=models.BigIntegerField(default=1572399236.746786),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_ds_smartwatch',
            field=models.BigIntegerField(default=1572399236.746786),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_login_datetime',
            field=models.BigIntegerField(default=1572399236.746786),
        ),
        migrations.AlterField(
            model_name='participant',
            name='register_datetime',
            field=models.BigIntegerField(default=1572399236.746786),
        ),
    ]
