from django.contrib import admin

from .models import Stock, UserStock

# Register your models here.


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    fields = ['name', 'full_name', 'stock_type', 'price']
    list_display = ['name', 'full_name', 'stock_type', 'price']
    search_fields = ['name', 'fullname', 'price']
    list_filter = ['stock_type']
    list_per_page = 10


@admin.register(UserStock)
class UserStockAdmin(admin.ModelAdmin):
    fields = ['stock', 'user', 'amount', 'profit']
    list_display = ['stock', 'user', 'amount', 'profit', 'date_created']
    list_filter = ['stock']
    search_fields = ['user']
    raw_id_fields = ['stock', 'user']
    list_per_page = 10
