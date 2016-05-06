# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0055_populate_step_broadcasts'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowrun',
            name='parent',
            field=models.ForeignKey(to='flows.FlowRun', help_text='The parent run that triggered us', null=True),
        ),
    ]
