from django.contrib import admin

from shop.models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available_dispaly', 'available_order', 'created', 'update']
    list_filter = ['available_display', 'created', 'update', 'category']
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Product, ProductAdmin)
