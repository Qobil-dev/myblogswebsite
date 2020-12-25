from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, null=True)
    info = models.TextField()
    short_info = models.TextField()
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    def slug(self):
        return slugify(self.name)

class CartInfo(models.Model):
    company_info = models.ForeignKey(CompanyInfo, on_delete=models.SET_NULL, blank=True, null=True)
    icon = models.ImageField(null=True, blank=True, upload_to='mycomp')
    info = models.TextField()
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.info

class Products(models.Model):
    name = models.CharField(max_length=200, null=True)
    photo = models.ImageField(null=False, blank=True, upload_to='media')
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

class Partners(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to='media')
    name = models.CharField(max_length=200, null=True)
    last_update = models.DateTimeField(auto_now_add=True)

class Contacts(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now_add=True)

class SocialMedia(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to='mycomp')
    link = models.CharField(max_length=200)
    last_update = models.DateTimeField(auto_now_add=True)