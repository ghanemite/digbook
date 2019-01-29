# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0004_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='bookmarks',
            field=models.ManyToManyField(related_name='tags', to='bookmarks.Bookmark'),
        ),
    ]
