from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from devices_monitor.models import Device, Category, Brand, Organization, Product
from devices_monitor.forms import (
    DeviceModelForm,
    CategoryModelForm,
    BrandModelForm,
    OrganizationModelForm,
    ProductModelForm,
)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["device_count"] = Device.objects.count()
        context["category_count"] = Category.objects.count()
        context["brand_count"] = Brand.objects.count()
        context["product_count"] = Product.objects.count()
        context["organization_count"] = Organization.objects.count()

        # Exemplo: últimos 5 devices cadastrados
        context["recent_devices"] = Device.objects.select_related("product", "organization").order_by("-id")[:5]

        return context

# -------------------------
# CATEGORY
# -------------------------
class CategoryListView(ListView):
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "categories"

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category_list")

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryModelForm
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category_list")

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/category_delete.html"
    success_url = reverse_lazy("category_list")

class CategoryDetailView(DetailView):
    model = Category
    template_name = "categories/category_detail.html"
    context_object_name = "category"


# -------------------------
# BRAND
# -------------------------
class BrandListView(ListView):
    model = Brand
    template_name = "brands/brand_list.html"
    context_object_name = "brands"

class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandModelForm
    template_name = "brands/brand_form.html"
    success_url = reverse_lazy("brand_list")

class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandModelForm
    template_name = "brands/brand_form.html"
    success_url = reverse_lazy("brand_list")

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = "brands/brand_delete.html"
    success_url = reverse_lazy("brand_list")

class BrandDetailView(DetailView):
    model = Brand
    template_name = "brands/brand_detail.html"
    context_object_name = "brand"


# -------------------------
# ORGANIZATION
# -------------------------
class OrganizationListView(ListView):
    model = Organization
    template_name = "organizations/organization_list.html"
    context_object_name = "organizations"

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationModelForm
    template_name = "organizations/organization_form.html"
    success_url = reverse_lazy("organization_list")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationModelForm
    template_name = "organizations/organization_form.html"
    success_url = reverse_lazy("organization_list")

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "organizations/organization_delete.html"
    success_url = reverse_lazy("organization_list")

class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organizations/organization_detail.html"
    context_object_name = "organization"


# -------------------------
# PRODUCT
# -------------------------
class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("product_list")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("product_list")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = reverse_lazy("product_list")

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


# -------------------------
# DEVICE
# -------------------------
class DeviceListView(ListView):
    model = Device
    template_name = "devices/device_list.html"
    context_object_name = "devices"

class DeviceCreateView(CreateView):
    model = Device
    form_class = DeviceModelForm
    template_name = "devices/device_form.html"
    success_url = reverse_lazy("device_list")

class DeviceUpdateView(UpdateView):
    model = Device
    form_class = DeviceModelForm
    template_name = "devices/device_form.html"
    success_url = reverse_lazy("device_list")

class DeviceDeleteView(DeleteView):
    model = Device
    template_name = "devices/device_delete.html"
    success_url = reverse_lazy("device_list")

class DeviceDetailView(DetailView):
    model = Device
    template_name = "devices/device_detail.html"
    context_object_name = "device"
