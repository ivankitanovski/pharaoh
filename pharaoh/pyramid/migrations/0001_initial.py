# Generated by Django 3.1.7 on 2021-03-18 19:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('points', models.FloatField(default=0, verbose_name='Points')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyramid.agent', verbose_name='Mentor')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level', models.IntegerField(primary_key=True, serialize=False, verbose_name='Level')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('points_from', models.FloatField(default=0, verbose_name='Points From')),
                ('points_to', models.FloatField(default=0, verbose_name='Points To')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('coefficient', models.FloatField(blank=True, null=True, verbose_name='Points coefficient')),
                ('adds_to_points', models.BooleanField(default=True, verbose_name='Adds points')),
                ('adds_to_payment', models.BooleanField(default=True, verbose_name='Adds points')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyramid.agent', verbose_name='Agent')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyramid.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('month', models.DateField(blank=True, default=datetime.datetime.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyramid.agent', verbose_name='Agent')),
            ],
        ),
    ]
