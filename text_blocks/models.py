from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .settings import CACHE_PREFIX


class TextBlock(models.Model):
    """
    A TextBlock is for pieces of content on the site that need to be edited.
    It is identified by a slug and has an optional header
    """
    slug = models.CharField(max_length=255, unique=True,
                help_text="A unique name to identify the block")
    header = models.CharField(blank=True, null=True, max_length=255,
                help_text="An optional header for this content")
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % (self.slug,)

    class Meta:
        verbose_name = 'Text Block'
        verbose_name_plural = 'Text Blocks'

@receiver([post_save, post_delete], sender=TextBlock)
def clear_textblock_cache(sender, instance, **kwargs):
    cache_key = '%s:%s' % (CACHE_PREFIX, instance.slug)
    cache.delete(cache_key)
