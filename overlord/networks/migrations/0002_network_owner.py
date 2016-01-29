# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('networks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, related_name='snippets'),
            preserve_default=False,
        ),
    ]