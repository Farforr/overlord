# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Minion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.SlugField(validators=[django.core.validators.MinLengthValidator(1)], max_length=45)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('top_level', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(related_name='minions', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(to='minions.Minion', blank=True, related_name='minions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MinionData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('field_name', models.CharField(max_length=80)),
                ('field_value', models.CharField(max_length=80)),
                ('owner', models.ForeignKey(related_name='data', to='minions.Minion')),
            ],
        ),
        migrations.CreateModel(
            name='MinionRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('response', models.BooleanField(default=True)),
                ('direction', models.CharField(choices=[('inc', 'incoming'), ('out', 'outgoing')], max_length=8)),
                ('owner', models.ForeignKey(related_name='requests', to='minions.Minion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MinionRequestBody',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('value', models.TextField()),
                ('request', models.OneToOneField(to='minions.MinionRequest', related_name='body')),
            ],
        ),
        migrations.CreateModel(
            name='MinionRequestHeader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=80)),
                ('value', models.CharField(max_length=80)),
                ('request', models.ForeignKey(related_name='headers', to='minions.MinionRequest')),
            ],
        ),
        migrations.AddField(
            model_name='miniondata',
            name='source',
            field=models.ForeignKey(related_name='data', to='minions.MinionRequest'),
        ),
    ]
