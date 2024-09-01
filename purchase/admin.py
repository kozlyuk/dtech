""" Admin configuration for Purchases app """

from django.contrib import admin

from .models import Order
from product.models import Device

class DeviceInline(admin.TabularInline):
    model = Device
    fields = ['executor', 'configuration']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['deal_number', 'customer', 'company', 'number_of_devices', 'status']
    list_filter = ['customer', 'company', 'status']
    search_fields = ['deal_number']
    inlines = [DeviceInline]
