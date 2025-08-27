"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from devices_monitor.views import (
    #HomePage
    HomePageView,    
    # Category
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    # Brand
    BrandListView, BrandCreateView, BrandUpdateView, BrandDeleteView,
    # Organization
    OrganizationListView, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    # Product
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    # Device
    DeviceListView, DeviceCreateView, DeviceUpdateView, DeviceDeleteView, DeviceDetailView,
)
from accounts.views import register_view, login_view, logout_view  # se você tiver auth separado

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", HomePageView.as_view(), name="home"),


    # Auth
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    # Devices
    path("devices/", DeviceListView.as_view(), name="device_list"),
    path("devices/add/", DeviceCreateView.as_view(), name="device_form"),
    path("devices/<int:pk>/", DeviceDetailView.as_view(), name="device_detail"),
    path("devices/update/<int:pk>/", DeviceUpdateView.as_view(), name="device_update"),
    path("devices/delete/<int:pk>/", DeviceDeleteView.as_view(), name="device_delete"),

    # Categories
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/add/", CategoryCreateView.as_view(), name="category_form"),
    path("categories/update/<int:pk>/", CategoryUpdateView.as_view(), name="category_update"),
    path("categories/delete/<int:pk>/", CategoryDeleteView.as_view(), name="category_delete"),

    # Brands
    path("brands/", BrandListView.as_view(), name="brand_list"),
    path("brands/add/", BrandCreateView.as_view(), name="brand_form"),
    path("brands/update/<int:pk>/", BrandUpdateView.as_view(), name="brand_update"),
    path("brands/delete/<int:pk>/", BrandDeleteView.as_view(), name="brand_delete"),

    # Organizations
    path("organizations/", OrganizationListView.as_view(), name="organization_list"),
    path("organizations/add/", OrganizationCreateView.as_view(), name="organization_form"),
    path("organizations/update/<int:pk>/", OrganizationUpdateView.as_view(), name="organization_update"),
    path("organizations/delete/<int:pk>/", OrganizationDeleteView.as_view(), name="organization_delete"),

    # Products
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/add/", ProductCreateView.as_view(), name="product_form"),
    path("products/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("products/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
