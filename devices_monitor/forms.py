from django import forms
from devices_monitor.models import Product, Category, Brand, Organization, Device

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'   

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BrandForm(forms.ModelForm):
    class Meta: 
        model = Brand
        fields = '__all__'

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class DeviceForm(forms.ModelForm):
    class Meta:
        models = Device
        fields = '__all__'