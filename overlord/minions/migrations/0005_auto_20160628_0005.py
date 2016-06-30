# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('minions', '0004_auto_20160628_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minion',
            name='owner',
            field=models.ForeignKey(related_name='minions', to=settings.AUTH_USER_MODEL),
        ),
    ]
