from django.shortcuts import render
from .models import *
# Create your views here.

def info(request):
    product = Products.objects.all()
    context = {'product': product}
    return render(request, 'index.html', context)