from django.contrib import admin
from django.utils import timezone

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'date_update')

    def get_date_display(self, obj):
        return timezone.localtime(obj.date).strftime('%d-%m-%Y %H:%M:%S')

    def get_date_update_display(self, obj):
        return timezone.localtime(obj.date_update).strftime('%Y-%m-%d %H:%M:%S')

    get_date_display.short_description = 'Date'
    get_date_update_display.short_description = 'Date Update'

    list_display = ('id', 'name', 'category', 'price', 'get_date_display', 'get_date_update_display')

admin.site.register(Product, ProductAdmin)