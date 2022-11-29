from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def show(request, prod_id):
    return HttpResponse("This is product: %s " % prod_id)
