from django.contrib import admin
from .models import *

# Register your models here.

class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_update']

class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'info', 'last_update']

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_update']

class PartnersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_update']

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'last_update']

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'last_update']

admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(CartInfo, CartInfoAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)