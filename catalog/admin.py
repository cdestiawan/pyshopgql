# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Product, Category, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'slug', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    inlines = (ProductImageInline,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ['title']}
