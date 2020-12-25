from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    product = Products.objects.all()
    info = CompanyInfo.objects.get(pk=1)
    cart_info = CartInfo.objects.get(pk=1)
    partners = Partners.objects.all()
    contact = Contacts.objects.get(pk=1)
    social_media = SocialMedia.objects.get(pk=1)
    context = {'product': product,
               'info': info,
               'cart_info': cart_info,
               'partners': partners,
               'contact': contact,
               'social_media': social_media
               }
    print(context)
    return render(request, 'index.html', context)