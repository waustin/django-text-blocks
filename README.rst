======
Text Blocks
======

Text Blocks is a fork of django-flatblocks https://github.com/zerok/django-flatblocks
with frontend editing removed and tinymce supported added to the admin.


Installation
------------
1. Add text_blocks to your INSTALLED_APP settings
2. Sync the DB by either running ./manage.py syncdb or 
   ./manage.py migrate text_blocks

Usage
----------
Once you've created some instances of the ``text_blocks.models.TextBlock``
model, you can load it it using the ``text_block_tags`` templatetag-library::
    
    {% load text_block_tags %}
    
    <html>
        <head>
            <!-- ... -->
        </head>
        <body>
            <div id="page">
                <div id="main">
                    <!-- ... -->
                </div>
                <div id="sidebar">
                    {% textblock "page.info" %}
                </div>
            </div>
        </body>
    </html>

This way you can display a text block with the name 'page.info'. If you 
have the name of a block in a template variable, leave out the quotes.

This tag also accepts an optional argument where you can specify the number
of seconds, the that block should be cached::
    
    {% textblock "page.info" 3600 %}

Additionally you can also specify which template should be used to render the
textblock::
    
    {% textblock "page.info" using="my_template.html" %}
    # ...
    {% textblock "page.about" 3600 using="my_template.html" %}

As with the slug of the textblock also with the template name you have the
choice of using the literal name of the template or pass it to the templatetag
as a variable.



