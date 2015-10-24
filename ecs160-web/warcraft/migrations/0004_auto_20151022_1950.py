# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warcraft', '0003_auto_20151020_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='loss',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.FileField(upload_to=b'images', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
