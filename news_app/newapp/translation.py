""""""
"""" ****************************************** Модуль Д14 *********************************************************"""

from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(Category)
class PostTranslationOptions(TranslationOptions):
    fields = ('name',)
