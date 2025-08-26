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
    template_name = "categories/category_confirm_delete.html"
    success_url = reverse_lazy("category_list")