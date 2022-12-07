from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from .models import Product
from django.template import loader

# Create your views here.
def index(request):
    prodList = Product.objects.all()
    context = {
        'prodList': prodList
    }
    return render(request, 'core/index.html', context)

def detail(request, prodId):
    product = get_object_or_404(Product, id=prodId)
    return render(request, 'core/detail.html', {'product': product})

def cart(request):
    context = {}
    return render(request, 'core/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'core/checkout.html', context)