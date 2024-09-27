from modeltranslation.translator import translator, TranslationOptions
from .models import PostCategory, Post


class PostCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(PostCategory, PostCategoryTranslationOptions)
translator.register(Post, PostTranslationOptions)
