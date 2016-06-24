# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0002_network_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='owner',
            field=models.ForeignKey(related_name='networks', to=settings.AUTH_USER_MODEL),
        ),
    ]
