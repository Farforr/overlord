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
            name='Underling',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.SlugField(max_length=45, validators=[django.core.validators.MinLengthValidator(1)])),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('top_level', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(related_name='underlings', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(related_name='underlings', blank=True, to='underlings.Underling')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnderlingRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('response', models.BooleanField(default=True)),
                ('direction', models.CharField(choices=[('inc', 'incoming'), ('out', 'outgoing')], max_length=8)),
                ('owner', models.ForeignKey(related_name='requests', to='underlings.Underling')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnderlingRequestBody',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('value', models.TextField()),
                ('request', models.OneToOneField(related_name='body', to='underlings.UnderlingRequest')),
            ],
        ),
        migrations.CreateModel(
            name='UnderlingRequestHeader',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
                ('value', models.CharField(max_length=80)),
                ('request', models.ForeignKey(related_name='headers', to='underlings.UnderlingRequest')),
            ],
        ),
    ]
