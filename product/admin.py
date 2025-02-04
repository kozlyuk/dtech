""" Admin configuration for Product app """

from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponseRedirect

from product.models import ComponentType, Component, Configuration, Device, Event
from product.forms import ChangeOrderForm, AddEventForm

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
    fields = ['event', 'date', 'comment', 'creator']
    readonly_fields = ['creator']
    extra = 0


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'configuration', 'executor', 'order', 'status']
    list_filter = ['configuration', 'executor', 'status']
    search_fields = ['serial_number', 'order__deal_number']
    exclude = ['creator']
    readonly_fields = ['serial_number', 'status']
    inlines = [EventInline]
    actions=['change_order','add_event']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()


    @admin.action(description='Змінити замовлення')
    def change_order(self, request, queryset):
        form = None

        if 'apply' in request.POST:
            form = ChangeOrderForm(request.POST)
            
            if form.is_valid():
                order = form.cleaned_data['order']
                queryset.update(order=order)
                
            self.message_user(request,
                              "Changed order on {} devices".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
        
        if not form:
            form = ChangeOrderForm(initial={'_selected_action': request.POST.getlist("_selected_action")})
                        
        return render(request,
                      'admin/order_intermediate.html',
                      {'items': queryset, 'form': form, 'title': 'Змінити замовлення'})


    @admin.action(description='Додати подію')
    def add_event(self, request, queryset):
        form = None

        if 'apply' in request.POST:
            form = AddEventForm(request.POST)
            
            if form.is_valid():
                event = form.cleaned_data['event']
                date = form.cleaned_data['date']
                comment = form.cleaned_data['comment']
                for device in queryset:
                    Event.objects.create(device=device,
                                         event=event,
                                         date=date,
                                         comment=comment)
                
            self.message_user(request,
                              "Added event to {} devices".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
        
        if not form:
            form = AddEventForm(initial={'_selected_action': request.POST.getlist("_selected_action")})
                        
        return render(request,
                      'admin/add_event.html',
                      {'items': queryset, 'form': form, 'title': 'Додати подію'})    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['device', 'event', 'date', 'creator', 'get_configuration', 'comment']
    search_fields = ['device__serial_number']
    list_filter = ['event', 'creator']
    date_hierarchy = 'date'

    def get_configuration(self, obj):
        return obj.device.configuration
    get_configuration.short_description = 'Configuration'
