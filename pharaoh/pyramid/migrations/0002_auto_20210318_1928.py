# Generated by Django 3.1.7 on 2021-03-18 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyramid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='month',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
