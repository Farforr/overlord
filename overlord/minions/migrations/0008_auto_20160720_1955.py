# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minions', '0007_auto_20160629_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minionrequest',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='minionrequestbody',
            name='request',
        ),
        migrations.RemoveField(
            model_name='minionrequestheader',
            name='request',
        ),
        migrations.RemoveField(
            model_name='miniondata',
            name='request',
        ),
        migrations.DeleteModel(
            name='MinionRequest',
        ),
        migrations.DeleteModel(
            name='MinionRequestBody',
        ),
        migrations.DeleteModel(
            name='MinionRequestHeader',
        ),
    ]
