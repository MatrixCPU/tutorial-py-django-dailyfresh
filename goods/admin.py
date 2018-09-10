from django.contrib import admin
from .models import GoodsCategory, GoodsItem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ItemAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name', 'price', 'unit', 'click', 'in_stock', 'category']


admin.site.register(GoodsCategory, CategoryAdmin)
admin.site.register(GoodsItem, ItemAdmin)
