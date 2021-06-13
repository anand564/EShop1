from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product

# Create your views here.

#def index(request):
    #return render(request, 'orders/order.html')

def index(request):
    prds = Product.get_all_products()
    print(prds)
    return render(request, 'index.html', {'products': prds})


