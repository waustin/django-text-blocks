#!/usr/bin/env python
# Bootstrap script for making migrations on a stand alone app
import sys
import django

from django.conf import settings
from django.core.management import call_command

settings.configure(DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'text_blocks',
    ),
)

django.setup()
call_command('makemigrations', 'text_blocks')
