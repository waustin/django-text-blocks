from django.contrib import admin
from django import forms
from django.conf import settings

from .models import TextBlock


class TextBlockAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.widgets.Textarea(
        attrs={'class': 'mceSimple', 'size': '40'}))

    class Meta:
        model = TextBlock


class TextBlockAdmin(admin.ModelAdmin):
    ordering = ['slug', ]
    list_display = ('slug', 'header')
    search_fields = ('slug', 'header', 'content')

    form = TextBlockAdminForm

    class Media:
        js = (settings.STATIC_URL + '/js/tiny_mce/tiny_mce.js',
              settings.STATIC_URL + '/js/tiny_mce_simple_init.js')

admin.site.register(TextBlock, TextBlockAdmin)
