from django import forms
from devices_monitor.models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        