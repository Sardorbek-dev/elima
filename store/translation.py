from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Product, Services, Cases


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class ServicesTranslationOptions(TranslationOptions):
    fields = ('title',)


class CasesTranslationOptions(TranslationOptions):
    fields = ('title',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'short_content', 'description', 'size', 'material', 'warming_material', 'filling', 'hood',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Services, ServicesTranslationOptions)
translator.register(Cases, CasesTranslationOptions)