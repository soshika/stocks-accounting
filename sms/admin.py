from django.contrib import admin

# Register your models here.


class SMSAdmin(admin.ModelAdmin):
    fields = ['message', 'status', 'date_created']
    list_display = ['message', 'status', 'date_created']
    list_filter = ['status', 'date_created']
    search_fields = ['message']
    list_per_page = 10