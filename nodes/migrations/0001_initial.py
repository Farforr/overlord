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
            name='Node',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.SlugField(validators=[django.core.validators.MinLengthValidator(1)], max_length=45)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('network', models.ForeignKey(to='networks.Network')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
