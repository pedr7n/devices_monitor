from django.contrib import admin
from devices_monitor.models import Brand, Category, Product, Organization, Device


# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('product', 'organization', 'category', 'serial', 'mac_address', 'local', 'admin', 'activation_flag', 'days_until_expiration')
    search_fields = ['product']

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'meraki_id', 'address', 'cnpj', 'account_manager', 'activation_flag', 'zoox_flag', 'propz_flag', 'iatec_flag', 'status_report_flag')
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'brand')
    search_fields = ['name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']



admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Device, DeviceAdmin)
