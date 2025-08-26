from django.views.generic import ListView, CreateView, DeleteView
from devices_monitor.models import Product, Device
from devices_monitor.forms import ProductModelForm

# Create your views here.

class DevicesListView(ListView):
    model = Device
    template_name = 'index.html'
    context_object_name = 'device'

    def get_queryset(self):
        device = super().get_queryset().order_by('product')
        search = self.request.GET.get('search')
        if search:
            device = device.filter(model__icontains=search)
        return device

class CreateDevice(CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'index.html'
    success_url = '/devices/'

