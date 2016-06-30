# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('minions', '0002_auto_20160627_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniondata',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 27, 22, 35, 6, 126028, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='miniondata',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 27, 22, 35, 10, 430142, tzinfo=utc), verbose_name='last modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minionrequestbody',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 27, 22, 35, 19, 582085, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minionrequestbody',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 27, 22, 35, 25, 342014, tzinfo=utc), verbose_name='last modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minionrequestheader',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 27, 22, 35, 29, 933939, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minionrequestheader',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 27, 22, 35, 35, 590038, tzinfo=utc), verbose_name='last modified'),
            preserve_default=False,
        ),
    ]
