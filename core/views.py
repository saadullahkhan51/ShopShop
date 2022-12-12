from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from .models import Product
from django.template import loader
from django.views.generic import ListView, DetailView

# def index(request):
#     prodList = Product.objects.all()
#     context = {
#         'prodList': prodList
#     }
#     return render(request, 'core/index.html', context)

class ProductListView(ListView):
    model = Product
    template_name: str = 'core/index.html'

class ProductDetailView(DetailView):
    model = Product
    template_name: str = 'core/detail.html'

# def detail(request, prodId):
#     product = get_object_or_404(Product, id=prodId)
#     return render(request, 'core/detail.html', {'product': product})

def cart(request):
    context = {}
    return render(request, 'core/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'core/checkout.html', context)