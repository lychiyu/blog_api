from django.contrib import admin

# Register your models here.
from article.models import Image, Article


@admin.register(Image)
class ImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'type', 'create_time')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cate', 'states', 'is_about', 'create_time', 'update_time')
