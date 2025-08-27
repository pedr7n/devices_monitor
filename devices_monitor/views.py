from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from devices_monitor.models import Product, Device, Category, Organization, Brand
from devices_monitor.forms import ProductForm

# Create your views here.

class CategoryListView(ListView):
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "categories"

class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category_list")

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category_list")

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/remove_category.html"
    success_url = reverse_lazy("category_list")

class DeviceListView(ListView):
    model = Device
    template_name = "devices/device_list.html"
    context_object_name = "devices"

class DeviceCreateView(CreateView):
    model = Device
    template_name = "devices/new_device.html"
    success_url = reverse_lazy("device_list")

class DeviceUpdateView(UpdateView):
    model = Device
    template_name = "devices/new_device.html"
    success_url = reverse_lazy("device_list")

class DeviceDeleteView(DeleteView):
    model = Device
    template_name = "devices/remove_device.html"