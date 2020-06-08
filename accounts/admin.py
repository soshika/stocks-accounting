from django.contrib import admin

from .models import Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'phone']
    list_display = ['first_name', 'last_name', 'username', 'phone']
    search_fields = ['first_name', 'last_name', 'username', 'phone']
    list_per_page = 10
