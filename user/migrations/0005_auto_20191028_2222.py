# Generated by Django 2.2.4 on 2019-10-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20191027_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='heartbeat_smartphone',
            field=models.BigIntegerField(default=1572268955.349863),
        ),
        migrations.AlterField(
            model_name='participant',
            name='heartbeat_smartwatch',
            field=models.BigIntegerField(default=1572268955.349863),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_ds_smartphone',
            field=models.BigIntegerField(default=1572268955.349863),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_ds_smartwatch',
            field=models.BigIntegerField(default=1572268955.349863),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_login_datetime',
            field=models.BigIntegerField(default=1572268955.349863),
        ),
        migrations.AlterField(
            model_name='participant',
            name='register_datetime',
            field=models.BigIntegerField(default=1572268955.349863),
        ),
    ]
