""" Admin configuration for Product app """

from django.contrib import admin

from product.models import ComponentType, Component, Configuration, Device, Event

@admin.register(ComponentType)
class ComponentTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name', 'component_type']
    list_filter = ['component_type__name']
    search_fields = ['name', 'short_description']
    exclude = ['creator']
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    exclude = ['creator']
    filter_horizontal = ['components', ]
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()
        

class EventInline(admin.TabularInline):
    model = Event
    fields = ['event', 'date', 'comment']
    extra = 0


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'configuration', 'executor', 'order', 'status']
    list_filter = ['configuration', 'executor', 'status']
    search_fields = ['serial_number', 'order']
    exclude = ['creator']
    readonly_fields = ['status']
    inlines = [EventInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()
