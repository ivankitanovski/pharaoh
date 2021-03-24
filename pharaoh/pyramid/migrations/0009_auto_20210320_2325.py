# Generated by Django 3.1.7 on 2021-03-20 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyramid', '0008_auto_20210320_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.FloatField(blank=True, verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='career_points',
            field=models.FloatField(blank=True, null=True, verbose_name='Total career points'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='compensation',
            field=models.FloatField(blank=True, null=True, verbose_name='Compensation'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='fiscal_points',
            field=models.FloatField(blank=True, null=True, verbose_name='Fiscal points'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='production_points',
            field=models.FloatField(blank=True, null=True, verbose_name='Production points'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='reward_points',
            field=models.FloatField(blank=True, null=True, verbose_name='Reward points'),
        ),
    ]
