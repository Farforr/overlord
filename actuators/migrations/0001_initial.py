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
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.SlugField(max_length=45, validators=[django.core.validators.MinLengthValidator(1)])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActuatorData',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('value', models.IntegerField()),
                ('actuator', models.ForeignKey(to='actuators.Actuator')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActuatorType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.SlugField(max_length=45, validators=[django.core.validators.MinLengthValidator(1)])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('manufacturer', models.CharField(max_length=45)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='actuator',
            name='model',
            field=models.ForeignKey(to='actuators.ActuatorType'),
        ),
        migrations.AddField(
            model_name='actuator',
            name='node',
            field=models.ForeignKey(to='nodes.Node'),
        ),
    ]
