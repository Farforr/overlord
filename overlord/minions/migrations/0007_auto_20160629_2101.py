# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minions', '0006_remove_minion_top_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='miniondata',
            old_name='owner',
            new_name='minion',
        ),
        migrations.RenameField(
            model_name='miniondata',
            old_name='source',
            new_name='request',
        ),
        migrations.AlterField(
            model_name='minionrequest',
            name='direction',
            field=models.CharField(choices=[('inc', 'Incoming'), ('out', 'Outgoing')], max_length=8),
        ),
    ]
