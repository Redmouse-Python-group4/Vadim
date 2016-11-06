# -*- coding: UTF-8 -*-
from django.contrib import admin

from .models import Article, Category
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date')
    list_filter = ['pub_date', 'category', 'is_active']
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
