# Generated by Django 2.2.5 on 2021-01-02 06:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 6, 50, 50, 896970, tzinfo=utc)),
        ),
    ]
