from django import forms
from devices_monitor.models import Product, Category, Brand, Organization, Device

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'   

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BrandModelForm(forms.ModelForm):
    class Meta: 
        model = Brand
        fields = '__all__'

class OrganizationModelForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class DeviceModelForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'