# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minions', '0005_auto_20160628_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minion',
            name='top_level',
        ),
    ]
