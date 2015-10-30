# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField(validators=[django.core.validators.MinLengthValidator(1)], max_length=45)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('value', models.IntegerField()),
                ('sensor', models.ForeignKey(to='sensors.Sensor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField(validators=[django.core.validators.MinLengthValidator(1)], max_length=45)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('manufacturer', models.CharField(max_length=45)),
                ('units', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='sensor',
            name='model',
            field=models.ForeignKey(to='sensors.SensorType'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='node',
            field=models.ForeignKey(to='nodes.Node'),
        ),
    ]
