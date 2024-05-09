""" Admin configuration for Product app """

from django.contrib import admin

from product.models import ComponentType, Component, Configuration, Device

@admin.register(ComponentType)
class ComponentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    exclude = ['creator']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    exclude = ['creator']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()
        
        
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    exclude = ['creator']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()
