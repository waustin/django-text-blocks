"""
The templatetag "textblock" lets you embed text-snippets (like for example the help section of a page)
into a template.

It accepts 2 parameter:

    slug
        The slug/key of the text (for example 'contact_help'). There are two
        ways you can pass the slug to the templatetag: (1) by its name or
        (2) as a variable.

        If you want to pass it by name, you have to use quotes on it.
        Otherwise just use the variable name.

    cache_time
        The number of seconds that text should get cached after it has been
        fetched from the database.

        This field is option and defaults to no caching.

Example::

    {% load textblock_tags %}

    ...

    {% textblock 'contact_help' %}
    {% textblock name_in_variable %}

The 'flatblock' template tag acts like an inclusiontag and operates on the
``textblock/textblock.html`` template file, which gets (besides the global
context) also the ``textblock`` variable passed.

Compared to the original implementation this includes not only the block's
content but the whole object inclusing title, slug and id. This way you
can easily for example offer administrative operations (like editing)
within that template.

"""

from django import template
from django.template.loader import render_to_string
from django.core.cache import cache

from ..models import TextBlock
from ..settings import CACHE_PREFIX

register = template.Library()


@register.simple_tag(takes_context=True)
def textblock(context, slug, timeout=None, using='text_blocks/textblock.html'):

    if timeout:
        # Build Key from slug/evaluated/using
        cache_key = '%s:%s' % (CACHE_PREFIX, slug)
        result = cache.get(cache_key)
        if result is not None:
            return result

    try:
        textblock = TextBlock.objects.get(slug=slug)
    except TextBlock.DoesNotExist:
        return ''

    context.update({'textblock': textblock})
    result = render_to_string(using, context)
    context.pop()

    if timeout:
        cache.set(cache_key, result, timeout=float(timeout))

    return result
