""" Admin configuration for Product app """

from django.contrib import admin

from product.models import ComponentType, Component, Configuration, Device

@admin.register(ComponentType)
class ComponentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    pass

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass

# @admin.register(ProductInstance)
# class ProductInstanceAdmin(admin.ModelAdmin):
#     """ Admin settings for ProductInstance table """
#     list_display = [
#         "product",
#         "cylinder",
#         "diopter",
#         "price",
#         "quantity_in_hand",
#     ]
#     fieldsets = [
#         (None, {'fields': ['product',
#                            'cylinder',
#                            'diopter',
#                            'price',
#                            'quantity_in_hand',
#                            ]})
#     ]
#     readonly_fields = [
#         "product",
#         "cylinder",
#         "diopter",
#         "quantity_in_hand",
#     ]
#     list_filter = ('cylinder', 'diopter',)
#     ordering = ('pk',)

