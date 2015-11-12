# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agcal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True, serialize=False, primary_key=True),
        ),
    ]
