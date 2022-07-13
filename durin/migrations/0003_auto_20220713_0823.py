# Generated by Django 3.2.14 on 2022-07-13 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durin', '0002_client_throttlerate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='token',
            field=models.CharField(db_index=True, help_text='Token is auto-generated on save.', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='token_ttl',
            field=models.DurationField(default=datetime.timedelta(days=14), help_text='\n            Token Time To Live (TTL) in timedelta. Format: <code>DAYS HH:MM:SS</code>.\n            ', verbose_name='Token Time To Live (TTL)'),
        ),
    ]ad