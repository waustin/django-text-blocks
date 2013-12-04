from django.conf import settings

CACHE_PREFIX = getattr(settings, 'TEXTBLOCK_CACHE_PREFIX', 'textblocks_')
