from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        # print('cart: ', request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        # this below code is used when the session is cleared ther will be no cart in the session so it will through the error
        # there is no cart in the session during the get request
        # this below code will create the empty in the session so that error get solved 
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        # request.session.get('cart').clear()
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories
        print("you are :", request.session.get('email'))  # to see the email session of the customer
        # return render(request, 'orders/order.html',)
        return render(request, 'index.html', data)
