# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.SlugField(validators=[django.core.validators.MinLengthValidator(1)], max_length=45)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActuatorData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('value', models.IntegerField()),
                ('actuator', models.ForeignKey(to='devices.Actuator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActuatorType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.SlugField(validators=[django.core.validators.MinLengthValidator(1)], max_length=45)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('manufacturer', models.CharField(max_length=45)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.SlugField(validators=[django.core.validators.MinLengthValidator(1)], max_length=45)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('network', models.ForeignKey(to='networks.Network')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('value', models.IntegerField()),
                ('sensor', models.ForeignKey(to='devices.Sensor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
            field=models.ForeignKey(to='devices.SensorType'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='node',
            field=models.ForeignKey(to='devices.Node'),
        ),
        migrations.AddField(
            model_name='actuator',
            name='model',
            field=models.ForeignKey(to='devices.ActuatorType'),
        ),
        migrations.AddField(
            model_name='actuator',
            name='node',
            field=models.ForeignKey(to='devices.Node'),
        ),
    ]
