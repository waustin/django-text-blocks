# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(help_text=b'A unique name to identify the block', unique=True, max_length=255)),
                ('header', models.CharField(help_text=b'An optional header for this content', max_length=255, null=True, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Text Block',
                'verbose_name_plural': 'Text Blocks',
            },
        ),
    ]
