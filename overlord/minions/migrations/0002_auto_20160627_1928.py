# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minion',
            name='parent',
            field=models.ForeignKey(null=True, to='minions.Minion', related_name='minions', blank=True),
        ),
    ]
