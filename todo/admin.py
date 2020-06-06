from django.contrib import admin
from .models import ToDo

# Register your models here.


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    fields = ['text', 'done', 'date_created']
    list_display = ['text', 'done', 'date_created']
    list_filter = ['date_created', 'done']
    search_fields = ['text']
    list_per_page = 10
