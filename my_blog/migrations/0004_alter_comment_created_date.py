# Generated by Django 3.2.13 on 2023-03-07 20:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_auto_20230307_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 20, 47, 42, 807441, tzinfo=utc)),
        ),
    ]
