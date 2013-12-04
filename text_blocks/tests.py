from django import template
from django.test import TestCase
from django.core.cache import cache
from django import db

from .models import TextBlock
from .settings import CACHE_PREFIX


class BasicTextBlockTests(TestCase):

    def setUp(self):
        self.testblock = TextBlock.objects.create(
            slug='block',
            header='HEADER',
            content='CONTENT'
        )

    def testCacheReset(self):
        """
        Tests if TextBlock.save() resets the cache.
        """
        tpl = template.Template('{% load text_block_tags %}{% textblock "block" 60 %}')
        tpl.render(template.Context({}))

        cache_key = '%s:%s' % (CACHE_PREFIX, 'block')

        self.assertNotEqual(None, cache.get(cache_key))
        block = TextBlock.objects.get(slug='block')
        block.header = 'UPDATED'
        block.save()


class TextBlockTagTests(TestCase):
    def setUp(self):
        self.testblock = TextBlock.objects.create(
            slug='block',
            header='HEADER',
            content='CONTENT'
        )

    def testLoadingTaglib(self):
        """Tests if the taglib defined in this app can be loaded"""
        tpl = template.Template('{% load text_block_tags %}')
        tpl.render(template.Context({}))

    def testExistingTemplate(self):
        tpl = template.Template(
            '{% load text_block_tags %}{% textblock "block" %}')
        output = tpl.render(template.Context({}))
        self.assertIn(self.testblock.content, output)
        self.assertIn(self.testblock.slug, output)

    def testUsingMissingTemplate(self):
        tpl = template.Template('{% load text_block_tags %}{% textblock "block" using="missing_template.html" %}')
        exception = template.TemplateDoesNotExist
        self.assertRaises(exception, tpl.render, template.Context({}))

    def testSyntax(self):
        tpl = template.Template(
            '{% load text_block_tags %}{% textblock "block" %}')
        tpl.render(template.Context({}))
        tpl = template.Template(
            '{% load text_block_tags %}{% textblock "block" 123 %}')
        tpl.render(template.Context({}))
        tpl = template.Template('{% load text_block_tags %}{% textblock "block" using="text_blocks/textblock.html" %}')
        tpl.render(template.Context({}))
        tpl = template.Template('{% load text_block_tags %}{% textblock "block" 123 using="text_blocks/textblock.html" %}')
        tpl.render(template.Context({}))

    def testBlockAsVariable(self):
        tpl = template.Template(
            '{% load text_block_tags %}{% textblock blockvar %}')
        tpl.render(template.Context({'blockvar': 'block'}))
