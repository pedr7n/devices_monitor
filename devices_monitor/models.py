from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_category')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='product_brand')
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    meraki_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True, default='Vazio')
    account_manager = models.CharField(max_length=100, null=True)
    activation_flag = models.BooleanField(null=True)
    zoox_flag = models.BooleanField(null=True)
    propz_flag = models.BooleanField(null=True)
    iatec_flag = models.BooleanField(null=True)
    status_report_flag = models.BooleanField(null=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='device_product')
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='device_org')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='device_category')
    serial = models.CharField(max_length=100, null=True, unique=True)
    mac_address = models.CharField(max_length=100, null=True, unique=True)
    local = models.CharField(max_length=100, null=True)
    admin = models.CharField(max_length=100, null=True)
    activation_flag = models.BooleanField(null=True)
    license = models.CharField(null=True, unique=True, max_length=100)
    days_until_expiration = models.IntegerField(blank=True, null=True)
    


