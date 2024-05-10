""" Admin configuration for Structure app """

from django.contrib import admin

from .models import Company, Customer, Contractor

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    pass
