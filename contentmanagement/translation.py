from modeltranslation.translator import translator, TranslationOptions
from .models import MainCarouselItem, ProductsCarouselItem, CustomerReview, FAQ, ShowcaseProduct, ShowcaseCategory


class MainCarouselItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ProductsCarouselItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class CustomerReviewTranslationOptions(TranslationOptions):
    fields = ('customer_name', 'company_name', 'position', 'review_text')


class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


class ShowcaseCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class ShowcaseProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(MainCarouselItem, MainCarouselItemTranslationOptions)
translator.register(ProductsCarouselItem, ProductsCarouselItemTranslationOptions)
translator.register(CustomerReview, CustomerReviewTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)
translator.register(ShowcaseCategory, ShowcaseCategoryTranslationOptions)
translator.register(ShowcaseProduct, ShowcaseProductTranslationOptions)
