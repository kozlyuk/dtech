""" Admin configuration for Purchases app """

from django.contrib import admin

from .models import Order
from product.models import Device

class DeviceInline(admin.TabularInline):
    model = Device
    fields = ['serial_number', 'configuration', 'status']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [DeviceInline]